from django.test import TestCase


class FormsTest(TestCase):

    def test_upload_form(self):
        import os
        from feedshare.feedlists.forms import FeedListUploadForm
        from feedshare.feedlists.models import FeedList
        from django.core.files.uploadedfile import SimpleUploadedFile

        # empty
        form = FeedListUploadForm()
        self.assertFalse(form.is_valid())

        # valid
        upload_file_dir = os.path.dirname(os.path.dirname(__file__))
        upload_file_path = os.path.join(upload_file_dir, 'testupload.xml')
        open(upload_file_path, 'wb')
        upload_file = open(upload_file_path, 'rb')
        data = dict(
            slug='some-slug'
        )
        file_data = dict(
            file=SimpleUploadedFile(upload_file.name, upload_file.read())
        )
        form = FeedListUploadForm(data, file_data)
        #self.assertTrue(form.is_valid())

        # invalid slug 1
        data['slug'] = 'login'
        form = FeedListUploadForm(data, file_data)
        self.assertFalse(form.is_valid())

        # invalid slug 2
        data['slug'] = 'invalid*slug'
        form = FeedListUploadForm(data, file_data)
        self.assertFalse(form.is_valid())

        # missing file
        data['slug'] = 'some-slug'
        file_data['file'] = None
        form = FeedListUploadForm(data, file_data)
        self.assertFalse(form.is_valid())

    def test_link_form(self):
        from feedshare.feedlists.forms import FeedListLinkForm
        from feedshare.feedlists.models import FeedList

        # empty
        form = FeedListLinkForm()
        self.assertFalse(form.is_valid())

        # valid data
        data = dict(
            slug='some-slug',
            url='http://www.feedshare.net/'
        )

        # valid
        form = FeedListLinkForm(data)
        self.assertTrue(form.is_valid())

        # invalid slug 1
        data['slug'] = 'login'
        form = FeedListLinkForm(data)
        self.assertFalse(form.is_valid())

        # invalid slug 2
        data['slug'] = 'invalid*slug'
        form = FeedListLinkForm(data)
        self.assertFalse(form.is_valid())

        # invalid url
        data['slug'] = 'some-slug'
        data['url'] = 'not-a-url'
        form = FeedListLinkForm(data)
        self.assertFalse(form.is_valid())

        # no url
        data['slug'] = 'some-slug'
        data['url'] = None
        form = FeedListLinkForm(data)
        self.assertFalse(form.is_valid())

    def test_edit_form(self):
        from feedshare.feedlists.forms import FeedListEditForm
        from feedshare.feedlists.models import FeedList

        # empty
        form = FeedListEditForm()
        self.assertFalse(form.is_valid())

        # valid data
        data = dict(
            slug='some-slug',
            url='http://www.feedshare.net/'
        )

        # valid
        form = FeedListEditForm(data)
        self.assertTrue(form.is_valid())

        # invalid slug 1
        data['slug'] = 'login'
        form = FeedListEditForm(data)
        self.assertFalse(form.is_valid())

        # invalid slug 2
        data['slug'] = 'invalid*slug'
        form = FeedListEditForm(data)
        self.assertFalse(form.is_valid())

        # invalid url
        data['slug'] = 'some-slug'
        data['url'] = 'not-a-url'
        form = FeedListEditForm(data)
        self.assertFalse(form.is_valid())

        # no url
        data['slug'] = 'some-slug'
        data['url'] = None
        form = FeedListEditForm(data)
        self.assertFalse(form.is_valid())
