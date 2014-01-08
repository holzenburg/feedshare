from django.conf.urls import patterns, include, url
from django.views.generic.base import TemplateView
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns(
    '',

    url(r'^grappelli/', include('grappelli.urls')),
    url(r'^admin/', include(admin.site.urls)),

    url(r'^legal/$', TemplateView.as_view(
        template_name='general/legal.html'), name='legal'),
    url(r'^imprint/$', TemplateView.as_view(
        template_name='general/imprint.html'), name='imprint'),
    url(r'^privacy/$', TemplateView.as_view(
        template_name='general/privacy.html'), name='privacy'),
    url(r'^contribute/$', TemplateView.as_view(
        template_name='general/contribute.html'), name='contribute'),
    url(r'^', include('feedshare.feedlists.urls')),

) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
