from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    url(r'^$', 'feedlists.views.index', name='feedlists_index'),
    url(r'^share/$', 'feedlists.views.share', name='feedlists_share'),
    url(r'^popular/$', 'feedlists.views.popular', name='feedlists_popular'),
    url(r'^search/$', 'feedlists.views.search', name='feedlists_search'),
    url(r'^(?P<slug>[0-9A-Za-z\-\_]+)/edit/(?P<secret>[0-9A-Za-z]+)/$', 'feedlists.views.edit', name='feedlists_edit'),
    url(r'^(?P<slug>[0-9A-Za-z\-\_]+)/$', 'feedlists.views.view', name='feedlists_view'),
)
