import time

from django.core.management.base import BaseCommand, CommandError
from django.db import connection

from feedshare.feedlists.models import FeedList
from feedshare.feedlists.models import FeedListFeed
from feedshare.feedlists.models import Feed


class Command(BaseCommand):
    args = '<>'
    help = 'Rebuilds the popularity values for feedlists'

    def handle(self, *args, **options):

        feedlists = FeedList.objects.all()
        feedlists.update(votes=0, popularity_pt2_a=0,
                         popularity_pt2_b=0, popularity_hn=0)

        for feedlist in feedlists:
            self.stdout.write(u'Building feed popularity '
                              'with %s views for %s' %
                              (feedlist.views, feedlist))
            t = time.mktime(feedlist.datetime_created.timetuple())
            for x in range(0, feedlist.views):
                feedlist.vote(t)
            feedlist.save()
            self.stdout.write(u'... %s votes -> %s' % (
                feedlist.votes, feedlist.popularity_pt2_a))

        self.stdout.write(u'Finished')
