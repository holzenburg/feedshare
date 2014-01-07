from django.shortcuts import render
from django.shortcuts import redirect
from django.shortcuts import get_object_or_404
from django.http import HttpResponseForbidden
from django.contrib import messages
from django.db.models import Q

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
            Q(file__icontains=q)
        )).order_by('-views')[:100]
    return render(request, 'feedlists/search.html', dict(q=q, feedlists=feedlists))


def share(request):
    used_form = 'upload'
    
    if request.method == 'POST' and request.POST.get('form_type') == 'upload':
        used_form = 'upload'
        upload_form = FeedListUploadForm(request.POST, request.FILES)
        if upload_form.is_valid():
            feedlist = upload_form.save()
            if feedlist.update_feeds():
                messages.success(request, 'Your feed list has been imported successfully.')
                return redirect('feedlists_edit', slug=feedlist.slug, secret=feedlist.secret)
            else:
                messages.error(request, 'There was an error importing your feeds.')
    else:
        upload_form = FeedListUploadForm()
                
    if request.method == 'POST' and request.POST.get('form_type') == 'link':
        used_form = 'link'
        link_form = FeedListLinkForm(request.POST)
        if link_form.is_valid():
            feedlist = link_form.save()
            if feedlist.update_feeds():
                messages.success(request, 'Your feed list has been imported successfully.')
                return redirect('feedlists_edit', slug=feedlist.slug, secret=feedlist.secret)
            else:
                messages.error(request, 'There was an error importing your feeds.')
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
        messages.error(request, 'The secret key you provided is not valid for this feed list.')
        raise Http403
        
    if request.method == 'POST':
        form = FeedListEditForm(request.POST, request.FILES, instance=feedlist)
        if form.is_valid():
            feedlist = form.save()
            if feedlist.update_feeds():
                messages.success(request, 'The feed list has been updated successfully.')
            else:
                messages.error(request, 'There was an error importing your feeds.')
        else:
            messages.warning(request, 'There was an error updating your feed list.')
    else:
        form = FeedListEditForm(instance=feedlist)

    return render(request, 'feedlists/edit.html', dict(form=form, feedlist=feedlist))
    