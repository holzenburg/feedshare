from django.core.management.base import BaseCommand, CommandError
from django.db import connection

from feedlists.models import FeedList
from feedlists.models import FeedListFeed
from feedlists.models import Feed


class Command(BaseCommand):
    args = '<>'
    help = 'Deletes all feeds and builts them again from source (file or url)'

    def handle(self, *args, **options):

        Feed.objects.all().delete()
        FeedListFeed.objects.all().delete()

        success_count = 0
        error_count = 0

        for feedlist in FeedList.objects.all():
            self.stdout.write(u'Building %s' % feedlist)
            success = feedlist.update_feeds()
            if success:
                self.stdout.write(u'- Successfully rebuilt feeds for %s' % feedlist)
                success_count += 1
            else:
                self.stdout.write(u'- Could not rebuild feeds for %s' % feedlist)
                error_count += 1

        self.stdout.write('Finished with %s successes, %s errors.' % (success_count, error_count))