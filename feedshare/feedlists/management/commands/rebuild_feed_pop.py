import time

from django.core.management.base import BaseCommand, CommandError
from django.db import connection

from feedshare.feedlists.models import FeedList
from feedshare.feedlists.models import FeedListFeed
from feedshare.feedlists.models import Feed


class Command(BaseCommand):
    args = '<>'
    help = 'Rebuilds the popularity values for feeds'

    def handle(self, *args, **options):

        feeds = Feed.objects.all()
        feeds.update(votes=0, popularity_pt2_a=0,
                     popularity_pt2_b=0, popularity_hn=0)

        for feedlist in FeedList.objects.all():
            self.stdout.write(u'Building feed popularity with %s' % feedlist)
            t = time.mktime(feedlist.datetime_created.timetuple())
            for feed in feedlist.feeds.all():
                feed.vote(t)
                feed.save()

        self.stdout.write(u'Finished')
