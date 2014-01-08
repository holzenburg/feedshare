# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'Feed.popularity_pt2'
        db.delete_column(u'feedlists_feed', 'popularity_pt2')

        # Adding field 'Feed.votes'
        db.add_column(u'feedlists_feed', 'votes',
                      self.gf('django.db.models.fields.PositiveIntegerField')(default=0),
                      keep_default=False)

        # Adding field 'Feed.popularity_pt2_a'
        db.add_column(u'feedlists_feed', 'popularity_pt2_a',
                      self.gf('django.db.models.fields.FloatField')(default=0),
                      keep_default=False)

        # Adding field 'Feed.popularity_pt2_b'
        db.add_column(u'feedlists_feed', 'popularity_pt2_b',
                      self.gf('django.db.models.fields.FloatField')(default=0),
                      keep_default=False)

        # Deleting field 'FeedList.popularity_pt2'
        db.delete_column(u'feedlists_feedlist', 'popularity_pt2')

        # Adding field 'FeedList.votes'
        db.add_column(u'feedlists_feedlist', 'votes',
                      self.gf('django.db.models.fields.PositiveIntegerField')(default=0),
                      keep_default=False)

        # Adding field 'FeedList.popularity_pt2_a'
        db.add_column(u'feedlists_feedlist', 'popularity_pt2_a',
                      self.gf('django.db.models.fields.FloatField')(default=0),
                      keep_default=False)

        # Adding field 'FeedList.popularity_pt2_b'
        db.add_column(u'feedlists_feedlist', 'popularity_pt2_b',
                      self.gf('django.db.models.fields.FloatField')(default=0),
                      keep_default=False)


    def backwards(self, orm):
        # Adding field 'Feed.popularity_pt2'
        db.add_column(u'feedlists_feed', 'popularity_pt2',
                      self.gf('django.db.models.fields.PositiveIntegerField')(default=0),
                      keep_default=False)

        # Deleting field 'Feed.votes'
        db.delete_column(u'feedlists_feed', 'votes')

        # Deleting field 'Feed.popularity_pt2_a'
        db.delete_column(u'feedlists_feed', 'popularity_pt2_a')

        # Deleting field 'Feed.popularity_pt2_b'
        db.delete_column(u'feedlists_feed', 'popularity_pt2_b')

        # Adding field 'FeedList.popularity_pt2'
        db.add_column(u'feedlists_feedlist', 'popularity_pt2',
                      self.gf('django.db.models.fields.PositiveIntegerField')(default=0),
                      keep_default=False)

        # Deleting field 'FeedList.votes'
        db.delete_column(u'feedlists_feedlist', 'votes')

        # Deleting field 'FeedList.popularity_pt2_a'
        db.delete_column(u'feedlists_feedlist', 'popularity_pt2_a')

        # Deleting field 'FeedList.popularity_pt2_b'
        db.delete_column(u'feedlists_feedlist', 'popularity_pt2_b')


    models = {
        u'feedlists.feed': {
            'Meta': {'object_name': 'Feed'},
            'datetime_created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'popularity_hn': ('django.db.models.fields.FloatField', [], {'default': '0'}),
            'popularity_pt2_a': ('django.db.models.fields.FloatField', [], {'default': '0'}),
            'popularity_pt2_b': ('django.db.models.fields.FloatField', [], {'default': '0'}),
            'site_url': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'url': ('django.db.models.fields.TextField', [], {}),
            'votes': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'})
        },
        u'feedlists.feedlist': {
            'Meta': {'object_name': 'FeedList'},
            'author': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'author_email': ('django.db.models.fields.EmailField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'datetime_created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'datetime_process': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'datetime_updated': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'feeds': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['feedlists.Feed']", 'through': u"orm['feedlists.FeedListFeed']", 'symmetrical': 'False'}),
            'file': ('django.db.models.fields.files.FileField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'popularity_hn': ('django.db.models.fields.FloatField', [], {'default': '0'}),
            'popularity_pt2_a': ('django.db.models.fields.FloatField', [], {'default': '0'}),
            'popularity_pt2_b': ('django.db.models.fields.FloatField', [], {'default': '0'}),
            'processing_error': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'secret': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '255'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'views': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'votes': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'})
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