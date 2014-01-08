from django.shortcuts import render
from django.shortcuts import redirect
from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from django.http import HttpResponseForbidden
from django.http import HttpResponseBadRequest
from django.contrib import messages
from django.db.models import Q
from django.utils import simplejson

from taggit.models import Tag

from .models import FeedList
from .models import Feed
from .forms import FeedListUploadForm
from .forms import FeedListLinkForm
from .forms import FeedListEditForm


def index(request, *args, **kwargs):
    return render(request, 'feedlists/index.html')


def view(request, *args, **kwargs):
    feedlist = get_object_or_404(FeedList, slug=kwargs.get('slug'))
    feedlist.view()
    return render(request, 'feedlists/view.html', dict(feedlist=feedlist))


def popular(request, *args, **kwargs):
    feedlists = FeedList.objects.all().order_by('-views')[:10]
    return render(request, 'feedlists/popular.html', dict(feedlists=feedlists))


def search(request, *args, **kwargs):
    q = request.GET.get('q')
    feedlists = None
    if q and len(q):
        feedlists = FeedList.objects.filter(Q(
            Q(title__icontains=q) |
            Q(author__icontains=q) |
            Q(author_email__icontains=q) |
            Q(url__icontains=q) |
            Q(file__icontains=q) |
            Q(tags__name__icontains=q)
        )).order_by('-views')[:100]
    return render(request, 'feedlists/search.html',
                  dict(q=q, feedlists=feedlists))


def tag(request, *args, **kwargs):
    tag = kwargs.get('tag')
    if not tag:
        tag = request.GET.get('tag')
    feedlists = None
    feeds = None
    if tag and len(tag):
        feedlists = FeedList.objects.filter(
            tags__name__in=[tag]
        ).distinct()[0:100]
        feeds = Feed.objects.filter(
            feedlistfeed__tags__name__in=[tag]
        ).distinct()[0:100]
    return render(request, 'feedlists/tag.html',
                  dict(tag=tag, feedlists=feedlists, feeds=feeds))


def share(request):
    used_form = 'upload'

    if request.method == 'POST' and request.POST.get('form_type') == 'upload':
        used_form = 'upload'
        upload_form = FeedListUploadForm(request.POST, request.FILES)
        if upload_form.is_valid():
            feedlist = upload_form.save()
            if feedlist.update_feeds():
                messages.success(request,
                                 'Your feed list has been \
                                 imported successfully.')
                return redirect('feedlists_edit',
                                slug=feedlist.slug,
                                secret=feedlist.secret)
            else:
                messages.error(request,
                               'There was an error importing your feeds.')
    else:
        upload_form = FeedListUploadForm()

    if request.method == 'POST' and request.POST.get('form_type') == 'link':
        used_form = 'link'
        link_form = FeedListLinkForm(request.POST)
        if link_form.is_valid():
            feedlist = link_form.save()
            if feedlist.update_feeds():
                messages.success(request,
                                 'Your feed list has been \
                                 imported successfully.')
                return redirect('feedlists_edit',
                                slug=feedlist.slug,
                                secret=feedlist.secret)
            else:
                messages.error(request,
                               'There was an error importing your feeds.')
    else:
        link_form = FeedListLinkForm()

    return render(request, 'feedlists/share.html', dict(
        upload_form=upload_form,
        link_form=link_form,
        used_form=used_form
    ))


def edit(request, *args, **kwargs):
    feedlist = get_object_or_404(FeedList, slug=kwargs.get('slug'))
    secret = kwargs.get('secret')
    if secret != feedlist.secret:
        messages.error(request,
                       'The secret key you provided \
                       is not valid for this feed list.')
        raise Http403

    if request.method == 'POST':
        form = FeedListEditForm(request.POST, request.FILES, instance=feedlist)
        if form.is_valid():
            feedlist = form.save()
            if feedlist.update_feeds():
                messages.success(request,
                                 'The feed list has been \
                                 updated successfully.')
                form = FeedListEditForm(instance=feedlist)
            else:
                messages.error(request,
                               'There was an error importing your feeds.')
        else:
            messages.warning(request,
                             'There was an error updating your feed list.')
    else:
        form = FeedListEditForm(instance=feedlist)

    return render(request, 'feedlists/edit.html', dict(
        form=form,
        feedlist=feedlist
    ))


def autocomplete_tags(request):
    query = request.GET.get('q', None)
    if request.method != 'GET' or not query:
        return HttpResponseBadRequest()

    try:
        tags = Tag.objects.filter(
            name__istartswith=query).values_list('name', flat=True)
    except:
        tags = Tag.objects.language().filter(
            name__istartswith=query).values_list('name', flat=True)

    return HttpResponse(
        simplejson.dumps(list(tags)),
        mimetype='text/javascript')
