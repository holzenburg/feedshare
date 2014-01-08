from django.contrib import admin

from .models import FeedList
from .models import FeedListFeed
from .models import Feed


class FeedListAdmin(admin.ModelAdmin):
    list_display = (
        '__unicode__',
        'datetime_created',
        'views',
        'processing_error')
    list_filter = ('processing_error',)
admin.site.register(FeedList, FeedListAdmin)


class FeedAdmin(admin.ModelAdmin):
    pass
admin.site.register(Feed, FeedAdmin)
