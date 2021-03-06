# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'TaskStore.pebble_cards_enabled'
        db.add_column(u'taskmanager_taskstore', 'pebble_cards_enabled',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)

        # Adding field 'TaskStore.feed_enabled'
        db.add_column(u'taskmanager_taskstore', 'feed_enabled',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)


        # Changing field 'TaskStore.local_path'
        db.alter_column(u'taskmanager_taskstore', 'local_path', self.gf('django.db.models.fields.CharField')(max_length=255))

    def backwards(self, orm):
        # Deleting field 'TaskStore.pebble_cards_enabled'
        db.delete_column(u'taskmanager_taskstore', 'pebble_cards_enabled')

        # Deleting field 'TaskStore.feed_enabled'
        db.delete_column(u'taskmanager_taskstore', 'feed_enabled')


        # Changing field 'TaskStore.local_path'
        db.alter_column(u'taskmanager_taskstore', 'local_path', self.gf('django.db.models.fields.FilePathField')(path='/Users/acoddington/Documents/Projects/inthe.am/task_data', max_length=100))

    models = {
        u'auth.group': {
            'Meta': {'object_name': 'Group'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        u'auth.permission': {
            'Meta': {'ordering': "(u'content_type__app_label', u'content_type__model', u'codename')", 'unique_together': "((u'content_type', u'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Group']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Permission']"}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'taskmanager.taskstore': {
            'Meta': {'object_name': 'TaskStore'},
            'configured': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'feed_enabled': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'local_path': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'pebble_cards_enabled': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'secret_id': ('django.db.models.fields.CharField', [], {'max_length': '36', 'blank': 'True'}),
            'sms_whitelist': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'sync_enabled': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'taskrc_extras': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'twilio_auth_token': ('django.db.models.fields.CharField', [], {'max_length': '32', 'blank': 'True'}),
            'updated': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'task_stores'", 'to': u"orm['auth.User']"})
        },
        u'taskmanager.taskstoreactivitylog': {
            'Meta': {'unique_together': "(('store', 'md5hash'),)", 'object_name': 'TaskStoreActivityLog'},
            'count': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'error': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_seen': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'md5hash': ('django.db.models.fields.CharField', [], {'max_length': '32'}),
            'message': ('django.db.models.fields.TextField', [], {}),
            'store': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'log_entries'", 'to': u"orm['taskmanager.TaskStore']"})
        },
        u'taskmanager.usermetadata': {
            'Meta': {'object_name': 'UserMetadata'},
            'colorscheme': ('django.db.models.fields.CharField', [], {'default': "'dark-yellow-green.theme'", 'max_length': '255'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'tos_accepted': ('django.db.models.fields.DateTimeField', [], {'default': 'None', 'null': 'True'}),
            'tos_version': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'metadata'", 'unique': 'True', 'to': u"orm['auth.User']"})
        }
    }

    complete_apps = ['taskmanager']