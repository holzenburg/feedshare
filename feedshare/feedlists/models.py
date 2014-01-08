import os
import re
import uuid
import hashlib
import datetime
import urlparse
import time

from django.db import models
from django.core.urlresolvers import reverse
from django.utils.timezone import now

from taggit.managers import TaggableManager

import listparser

current_milli_time = lambda: int(round(time.time() * 1000))

POPULARITY_HN_GRAVITY = 1.2  # hn: 1.8


def get_upload_path(instance, filename):
    directory = instance.slug \
        or hashlib.md5(str(uuid.uuid4())).hexdigest()[0:10]
    return os.path.join('lists', directory, filename)

remove_email_re = re.compile(r'.*(([_a-z0-9-]+?(\.[_a-z0-9-]+?)*)@' +
                             '([a-z0-9-]+?(\.[a-z0-9-]+?)*(\.[a-z]{2,4}))).*')


def remove_email(string):
    result = remove_email_re.match(string)
    return string.replace('@%s' % result.groups()[3], '') if result else string


class PopularityModel(models.Model):
    datetime_created = models.DateTimeField(auto_now_add=True)
    votes = models.PositiveIntegerField(default=0)

    # http://stackoverflow.com/questions/11128086/simple-popularity-algorithm
    popularity_pt2_a = models.FloatField(default=0)
    popularity_pt2_b = models.FloatField(default=0)

    # http://amix.dk/blog/post/19574
    popularity_hn = models.FloatField(default=0)

    class Meta:
        abstract = True

    def vote(self, t=None):
        self.votes += 1
        if not t:
            t = float(current_milli_time())
        self.update_popularity_pt2_a(t)
        self.update_popularity_pt2_b(t)
        self.update_popularity_hn()

    def update_popularity_pt2_a(self, t):
        p = float(self.popularity_pt2_a)
        self.popularity_pt2_a = (p + t) / 2.0 if p else t

    def update_popularity_pt2_b(self, t):
        p = float(self.popularity_pt2_b)
        if p:
            self.popularity_pt2_b = (p + t) / 2.0
        else:
            initial = self.__class__.objects.aggregate(
                models.Avg('popularity_pt2_b')
            ).values()[0]
            self.popularity_pt2_b = initial if initial > 0 else t

    def update_popularity_hn(self):
        t = float((now() - self.datetime_created).seconds) / 3600
        p = (self.votes - 1) / ((t + 2) ** POPULARITY_HN_GRAVITY)
        self.popularity_hn = p


class FeedList(PopularityModel):
    slug = models.SlugField(
        max_length=255,
        unique=True,
        help_text='Part of the URL (http://feedshare.net/your-slug)')
    title = models.CharField(
        max_length=255,
        blank=True, null=True)
    description = models.TextField(
        blank=True, null=True)
    author = models.CharField(
        max_length=255,
        blank=True, null=True,
        verbose_name='Your name')
    author_email = models.EmailField(
        max_length=255,
        blank=True, null=True,
        verbose_name='Email address',
        help_text='Not public, just to recover the secret editing key')
    file = models.FileField(
        upload_to=get_upload_path,
        blank=True, null=True,
        verbose_name='OPML File')
    url = models.URLField(
        max_length=255,
        blank=True, null=True,
        verbose_name='OPML URL')
    secret = models.CharField(
        max_length=255)
    processing_error = models.BooleanField(
        blank=True,
        default=False)
    datetime_process = models.DateTimeField(
        blank=True, null=True)
    datetime_updated = models.DateTimeField(
        blank=True, null=True)
    views = models.PositiveIntegerField(
        default=0)

    feeds = models.ManyToManyField('Feed', through='FeedListFeed')
    tags = TaggableManager()

    class Meta:
        verbose_name = 'Feedlist'
        verbose_name_plural = 'Feedlist'

    def __unicode__(self):
        return remove_email(self.title if self.title else self.slug)

    def save(self, *args, **kwargs):
        if self.title and not len(self.title):
            self.title = None
        if not self.secret:
            self.secret = hashlib.md5(str(uuid.uuid4())).hexdigest()[0:10]
        super(FeedList, self).save(*args, **kwargs)

    def view(self):
        self.update_if_necessary()
        self.views += 1
        self.save()

    def get_absolute_url(self):
        return reverse('feedlists_view', kwargs=dict(
            slug=self.slug))

    def get_edit_url(self):
        return reverse('feedlists_edit', kwargs=dict(
            slug=self.slug,
            secret=self.secret))

    def filename(self):
        if self.file:
            return os.path.basename(self.file.name)

    def url_filename(self):
        if self.url:
            return os.path.basename(self.url)

    def update_if_necessary(self):
        if self.processing_error:
            aged = now() - datetime.timedelta(minutes=5)
            if not self.datetime_process or self.datetime_process < aged:
                self.update_feeds()
        elif self.url:
            aged = now() - datetime.timedelta(days=1)
            if not self.datetime_updated or self.datetime_updated < aged:
                success = self._process_url()
                self.update_success(success, save=False)
        return self.processing_error

    def update_feeds(self):
        success = False
        if self.url:
            success = self._process_url()
        elif self.file:
            success = self._process_file()
        self.update_success(success)
        return success

    def update_success(self, success, save=True):
        self.datetime_process = now()
        if success:
            self.processing_error = False
            self.datetime_updated = now()
        else:
            self.processing_error = True
        if save:
            self.save()
        return not self.processing_error

    def _process_url(self):
        url = str(self.url)
        result = listparser.parse(url)
        if result['bozo'] == 1:
            return False
        self._process_result(result)
        return True

    def _process_file(self):
        result = listparser.parse(self.file, 'feedshare.net')
        if result['bozo'] == 1 and not result['feeds']:
            return False
        self._process_result(result)
        return True

    def _process_result(self, result):
        if not self.pk:
            self.save()
        if (not self.title or not len(self.title)) and result.meta.title:
            self.title = result.meta.title

        feedlistfeed_pks = []

        for feed_data in result.feeds:
            feed, feed_created = Feed.objects\
                .get_or_create(
                    url=feed_data['url'],
                    defaults={'title': feed_data['title']})
            feedlistfeed, feedlistfeed_created = FeedListFeed.objects\
                .get_or_create(feed=feed, feedlist=self)
            if feedlistfeed_created:
                feed.vote()
            feedlistfeed.title = feed_data['title']
            feedlistfeed.tags.add(*[x.lower() for x in feed_data['tags']])
            feedlistfeed.save()
            feedlistfeed_pks.append(feedlistfeed.pk)

        FeedListFeed.objects.filter(feedlist=self)\
            .exclude(pk__in=feedlistfeed_pks)\
            .delete()


class FeedListFeed(models.Model):
    feedlist = models.ForeignKey('FeedList')
    feed = models.ForeignKey('Feed')
    title = models.CharField(max_length=255, blank=True, null=True)
    tags = TaggableManager()

    class Meta:
        verbose_name = 'Feedlist Feed'
        verbose_name_plural = 'Feedlist Feeds'

    def __unicode__(self):
        return unicode(self.title)


class Feed(PopularityModel):
    url = models.TextField()
    site_url = models.URLField(blank=True, null=True)
    title = models.CharField(max_length=255, blank=True, null=True)
    description = models.TextField(blank=True, null=True)

    class Meta:
        verbose_name = 'Feed'
        verbose_name_plural = 'Feeds'

    def __unicode__(self):
        return unicode(self.url)

    def save(self, *args, **kwargs):
        self.site_url = '{uri.scheme}://{uri.netloc}/'.format(
            uri=urlparse.urlparse(self.url))
        super(Feed, self).save(*args, **kwargs)
