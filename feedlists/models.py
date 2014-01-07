import os
import re
import uuid
import hashlib
import datetime
import urlparse

from django.db import models
from django.core.urlresolvers import reverse
from django.utils.timezone import now

import listparser


def get_upload_path(instance, filename):
    return os.path.join('lists', instance.slug, filename)

remove_email_re = re.compile(r'.*(([_a-z0-9-]+?(\.[_a-z0-9-]+?)*)@([a-z0-9-]+?(\.[a-z0-9-]+?)*(\.[a-z]{2,4}))).*')
      
def remove_email(string):
    result = remove_email_re.match(string)
    return string.replace('@%s' % result.groups()[3], '') if result else string


class FeedList(models.Model):
    slug = models.SlugField(max_length=255, unique=True, help_text='Part of the URL (http://feedshare.net/your-slug)')
    title = models.CharField(max_length=255, blank=True)
    description = models.TextField(blank=True)
    author = models.CharField(max_length=255, blank=True, verbose_name='Your name')
    author_email = models.EmailField(max_length=255, blank=True, verbose_name='Email address', help_text='Not public, just to recover the secret editing key')
    file = models.FileField(upload_to=get_upload_path, blank=True, verbose_name='OPML File')
    url = models.URLField(max_length=255, blank=True, verbose_name='OPML URL')
    secret = models.CharField(max_length=255)
    processing_error = models.BooleanField(blank=True, default=False)
    datetime_created = models.DateTimeField(auto_now_add=True)
    datetime_updated = models.DateTimeField(blank=True, null=True)
    views = models.PositiveIntegerField(default=0)

    def save(self, *args, **kwargs):
        if not self.secret:
            self.secret = hashlib.md5(str(uuid.uuid4())).hexdigest()[0:10]
        super(FeedList, self).save(*args, **kwargs)
    
    def __unicode__(self):
        return remove_email(self.title if self.title and len(self.title) else self.slug)
    
    def view(self):
        self.update_from_url_if_necessary()
        self.views += 1
        self.save()
    
    def get_absolute_url(self):
        return reverse('feedlists_view', kwargs=dict(slug=self.slug))

    def get_edit_url(self):
        return reverse('feedlists_edit', kwargs=dict(slug=self.slug, secret=self.secret))

    def filename(self):
        if self.file:
            return os.path.basename(self.file.name)

    def url_filename(self):
        if self.url:
            return os.path.basename(self.url)

    def update_feeds(self):
        success = False
        if self.url:
            success = self._process_url()
        elif self.file:
            success = self._process_file()
        self.update_success(success)
        return success
        
    def update_from_url_if_necessary(self):
        if self.url:
            if not self.datetime_updated or self.datetime_updated < now() - datetime.timedelta(days=7):
                success = self._process_url()
                self.update_success(success, save=False)
                return success
        return self.processing_error
    
    def update_success(self, success, save=True):
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
        if result['bozo'] == 1:
            return False
        self._process_result(result)
        return True
    
    def _process_result(self, result):
        if (not self.title or not len(self.title)) and result.meta.title:
            self.title = result.meta.title
            
        for feed_data in result.feeds:
            tags = []
            for tag in feed_data['tags']:
                if tag not in tags:
                    tags.append(tag)
            for category in feed_data['categories']:
                if tag not in tags:
                    tags.append(tag)

            feed, created = Feed.objects.get_or_create(feedlist=self, url=feed_data['url'])
            feed.title = feed_data['title']
            feed.tags = ','.join(tags)
            feed.save()


class Feed(models.Model):
    feedlist = models.ForeignKey(FeedList)
    url = models.TextField()
    title = models.CharField(max_length=255, blank=True)
    tags = models.TextField(blank=True)
    description = models.TextField(blank=True)

    def get_tags(self):
        return self.tags.split(',')

    def get_site_url(self):
        return '{uri.scheme}://{uri.netloc}/'.format(uri=urlparse.urlparse(self.url))
    