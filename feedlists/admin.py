from django.contrib import admin

from .models import FeedList
from .models import Feed


class FeedInlineAdmin(admin.TabularInline):
    model = Feed
    extra = 0

class FeedListAdmin(admin.ModelAdmin):
    list_display = ('__unicode__', 'datetime_created', 'views')
    inlines = [FeedInlineAdmin]
admin.site.register(FeedList, FeedListAdmin)


class FeedAdmin(admin.ModelAdmin):
    pass
admin.site.register(Feed, FeedAdmin)