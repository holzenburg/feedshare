from django import forms
from taggit.forms import TagField

from .models import FeedList
from .settings import FORBIDDEN_SLUGS


def _clean_slug(instance):
    data = instance.cleaned_data['slug']
    if data in FORBIDDEN_SLUGS:
        raise forms.ValidationError("This slug is not allowed!",
                                    code="invalid")
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

    tags = TagField(
        required=False,
        help_text="Please tag this list, yourself, "
                  "your industry and profession "
                  "to help others find your list."
    )

    def clean_url(self):
        data = self.cleaned_data['url']
        if not data and not self.cleaned_data['file']:
            raise forms.ValidationError(
                "You must upload a file or enter a valid URL")
        return data

    def clean_slug(self):
        return _clean_slug(self)

    class Meta:
        model = FeedList
        fields = [
            'slug',
            'title',
            'tags',
            'author',
            'author_email',
            'file',
            'url'
        ]
