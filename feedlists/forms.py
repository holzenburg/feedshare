from django import forms

from .models import FeedList

FORBIDDEN_SLUGS = [
    # brand
    'feedshare',
    'feedshare_net',
    'feedshare-net',
    # functional
    'share',
    'popular',
    'search'
    # content
    'about',
    'imprint',
    'privacy',
    'legal',
    'abuse',
    # accounts
    'account',
    'accounts',
    'login',
    'logout',
    # social
    'facebook',
    'twitter',
    'google',
    'google-plus',
]


def _clean_slug(instance):
    data = instance.cleaned_data['slug']
    if data in FORBIDDEN_SLUGS:
        raise forms.ValidationError("This slug is not allowed!", code="invalid")
    return data


class FeedListUploadForm(forms.ModelForm):

    file = forms.FileField(required=True)

    def clean_slug(self):
        return _clean_slug(self)
        
    class Meta:
        model = FeedList
        fields = ['slug', 'file']


class FeedListLinkForm(forms.ModelForm):
    
    url = forms.URLField(required=True)
    
    def clean_slug(self):
        return _clean_slug(self)
        
    class Meta:
        model = FeedList
        fields = ['slug', 'url']


class FeedListEditForm(forms.ModelForm):
    
    def clean(self):
        if not self.url and not self.file:
            raise ValidationError("You must upload a file or enter a valid URL")
            
    def clean_slug(self):
        return _clean_slug(self)
        
    class Meta:
        model = FeedList
        exclude = ['secret', 'processing_error', 'datetime_updated', 'views']

    