# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'Feedback.worthwile'
        db.delete_column(u'feedbackform_feedback', 'worthwile')

        # Adding field 'Feedback.worthwhile'
        db.add_column(u'feedbackform_feedback', 'worthwhile',
                      self.gf('django.db.models.fields.CharField')(default=1, max_length=50),
                      keep_default=False)


    def backwards(self, orm):
        # Adding field 'Feedback.worthwile'
        db.add_column(u'feedbackform_feedback', 'worthwile',
                      self.gf('django.db.models.fields.CharField')(default=1, max_length=50),
                      keep_default=False)

        # Deleting field 'Feedback.worthwhile'
        db.delete_column(u'feedbackform_feedback', 'worthwhile')


    models = {
        u'badgeclient.badgeservice': {
            'Meta': {'object_name': 'BadgeService'},
            'api_key': ('django.db.models.fields.CharField', [], {'max_length': '500'}),
            'app_id': ('django.db.models.fields.IntegerField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'url': ('django.db.models.fields.CharField', [], {'max_length': '500'})
        },
        u'feedbackform.event': {
            'Meta': {'object_name': 'Event'},
            'badge': ('django.db.models.fields.SlugField', [], {'max_length': '50'}),
            'badge_service': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['badgeclient.BadgeService']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        u'feedbackform.feedback': {
            'Meta': {'object_name': 'Feedback'},
            'date': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'null': 'True', 'blank': 'True'}),
            'empowered': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'event': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'improve': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'learned': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'nationality': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'organise': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'testimonial': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'useful': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'worthwhile': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        }
    }

    complete_apps = ['feedbackform']