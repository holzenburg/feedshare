from django.contrib import admin

from .models import FeedList
from .models import FeedListFeed
from .models import Feed


class FeedListAdmin(admin.ModelAdmin):
    list_display = (
        '__unicode__',
        'processing_error',
        'datetime_created',
        'views',
        'votes',
        'popularity_pt2_a',
        'popularity_pt2_b',
        'popularity_hn',
    )
    list_filter = ('processing_error',)
admin.site.register(FeedList, FeedListAdmin)


class FeedAdmin(admin.ModelAdmin):
    list_display = (
        '__unicode__',
        'datetime_created',
        'votes',
        'popularity_pt2_a',
        'popularity_pt2_b',
        'popularity_hn',
    )
admin.site.register(Feed, FeedAdmin)
