from django.conf.urls import patterns, include, url

urlpatterns = patterns(
    'feedshare.feedlists.views',

    url(r'^$', 'index', name='feedlists_index'),
    url(r'^share/$', 'share', name='feedlists_share'),
    url(r'^popular/$', 'popular', name='feedlists_popular'),
    url(r'^search/$', 'search', name='feedlists_search'),

    url(r'^autocomplete/tags/$',
        'autocomplete_tags', name='feedlists_autocomplete_tags'),
    url(r'^tags/$',
        'tag', name='feedlists_tags'),
    url(r'^tags/(?P<tag>.+)/$',
        'tag', name='feedlists_tag'),

    url(r'^(?P<slug>[0-9A-Za-z\-\_]+)/edit/(?P<secret>[0-9A-Za-z]+)/$',
        'edit', name='feedlists_edit'),
    url(r'^(?P<slug>[0-9A-Za-z\-\_]+)/$',
        'view', name='feedlists_view'),
)
