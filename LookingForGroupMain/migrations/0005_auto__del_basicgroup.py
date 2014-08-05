# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting model 'BasicGroup'
        db.delete_table(u'LookingForGroupMain_basicgroup')


    def backwards(self, orm):
        # Adding model 'BasicGroup'
        db.create_table(u'LookingForGroupMain_basicgroup', (
            ('users', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['UserProfile.UserProfile'])),
            ('description', self.gf('django.db.models.fields.TextField')()),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=256)),
            ('date_created', self.gf('django.db.models.fields.DateTimeField')()),
            ('date_action', self.gf('django.db.models.fields.DateTimeField')()),
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('group_size', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal(u'LookingForGroupMain', ['BasicGroup'])


    models = {
        
    }

    complete_apps = ['LookingForGroupMain']