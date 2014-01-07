# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'FeedListFeed'
        db.create_table(u'feedlists_feedlistfeed', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('feedlist', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['feedlists.FeedList'])),
            ('feed', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['feedlists.Feed'])),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
        ))
        db.send_create_signal(u'feedlists', ['FeedListFeed'])

        # Deleting field 'Feed.feedlist'
        db.delete_column(u'feedlists_feed', 'feedlist_id')

        # Deleting field 'Feed.tags'
        db.delete_column(u'feedlists_feed', 'tags')

        # Adding field 'Feed.site_url'
        db.add_column(u'feedlists_feed', 'site_url',
                      self.gf('django.db.models.fields.URLField')(max_length=200, null=True, blank=True),
                      keep_default=False)


        # Changing field 'Feed.description'
        db.alter_column(u'feedlists_feed', 'description', self.gf('django.db.models.fields.TextField')(null=True))

        # Changing field 'Feed.title'
        db.alter_column(u'feedlists_feed', 'title', self.gf('django.db.models.fields.CharField')(max_length=255, null=True))

        # Changing field 'FeedList.description'
        db.alter_column(u'feedlists_feedlist', 'description', self.gf('django.db.models.fields.TextField')(null=True))

        # Changing field 'FeedList.title'
        db.alter_column(u'feedlists_feedlist', 'title', self.gf('django.db.models.fields.CharField')(max_length=255, null=True))

        # Changing field 'FeedList.author_email'
        db.alter_column(u'feedlists_feedlist', 'author_email', self.gf('django.db.models.fields.EmailField')(max_length=255, null=True))

        # Changing field 'FeedList.url'
        db.alter_column(u'feedlists_feedlist', 'url', self.gf('django.db.models.fields.URLField')(max_length=255, null=True))

        # Changing field 'FeedList.author'
        db.alter_column(u'feedlists_feedlist', 'author', self.gf('django.db.models.fields.CharField')(max_length=255, null=True))

        # Changing field 'FeedList.file'
        db.alter_column(u'feedlists_feedlist', 'file', self.gf('django.db.models.fields.files.FileField')(max_length=100, null=True))

    def backwards(self, orm):
        # Deleting model 'FeedListFeed'
        db.delete_table(u'feedlists_feedlistfeed')


        # User chose to not deal with backwards NULL issues for 'Feed.feedlist'
        raise RuntimeError("Cannot reverse this migration. 'Feed.feedlist' and its values cannot be restored.")
        
        # The following code is provided here to aid in writing a correct migration        # Adding field 'Feed.feedlist'
        db.add_column(u'feedlists_feed', 'feedlist',
                      self.gf('django.db.models.fields.related.ForeignKey')(to=orm['feedlists.FeedList']),
                      keep_default=False)

        # Adding field 'Feed.tags'
        db.add_column(u'feedlists_feed', 'tags',
                      self.gf('django.db.models.fields.TextField')(default='', blank=True),
                      keep_default=False)

        # Deleting field 'Feed.site_url'
        db.delete_column(u'feedlists_feed', 'site_url')


        # Changing field 'Feed.description'
        db.alter_column(u'feedlists_feed', 'description', self.gf('django.db.models.fields.TextField')(default=''))

        # Changing field 'Feed.title'
        db.alter_column(u'feedlists_feed', 'title', self.gf('django.db.models.fields.CharField')(default='', max_length=255))

        # Changing field 'FeedList.description'
        db.alter_column(u'feedlists_feedlist', 'description', self.gf('django.db.models.fields.TextField')(default=''))

        # Changing field 'FeedList.title'
        db.alter_column(u'feedlists_feedlist', 'title', self.gf('django.db.models.fields.CharField')(default='', max_length=255))

        # Changing field 'FeedList.author_email'
        db.alter_column(u'feedlists_feedlist', 'author_email', self.gf('django.db.models.fields.EmailField')(default='', max_length=255))

        # Changing field 'FeedList.url'
        db.alter_column(u'feedlists_feedlist', 'url', self.gf('django.db.models.fields.URLField')(default='', max_length=255))

        # Changing field 'FeedList.author'
        db.alter_column(u'feedlists_feedlist', 'author', self.gf('django.db.models.fields.CharField')(default='', max_length=255))

        # User chose to not deal with backwards NULL issues for 'FeedList.file'
        raise RuntimeError("Cannot reverse this migration. 'FeedList.file' and its values cannot be restored.")
        
        # The following code is provided here to aid in writing a correct migration
        # Changing field 'FeedList.file'
        db.alter_column(u'feedlists_feedlist', 'file', self.gf('django.db.models.fields.files.FileField')(max_length=100))

    models = {
        u'feedlists.feed': {
            'Meta': {'object_name': 'Feed'},
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'site_url': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'url': ('django.db.models.fields.TextField', [], {})
        },
        u'feedlists.feedlist': {
            'Meta': {'object_name': 'FeedList'},
            'author': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'author_email': ('django.db.models.fields.EmailField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'datetime_created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'datetime_updated': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'feeds': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['feedlists.Feed']", 'through': u"orm['feedlists.FeedListFeed']", 'symmetrical': 'False'}),
            'file': ('django.db.models.fields.files.FileField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'processing_error': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'secret': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '255'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'views': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'})
        },
        u'feedlists.feedlistfeed': {
            'Meta': {'object_name': 'FeedListFeed'},
            'feed': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['feedlists.Feed']"}),
            'feedlist': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['feedlists.FeedList']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['feedlists']