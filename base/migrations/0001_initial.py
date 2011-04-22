# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'State'
        db.create_table('base_state', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
        ))
        db.send_create_signal('base', ['State'])

        # Adding model 'District'
        db.create_table('base_district', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('state', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['base.State'])),
        ))
        db.send_create_signal('base', ['District'])

        # Adding model 'Location'
        db.create_table('base_location', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('district', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['base.District'])),
        ))
        db.send_create_signal('base', ['Location'])

        # Adding model 'Level'
        db.create_table('base_level', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('grade_name', self.gf('django.db.models.fields.CharField')(max_length=10)),
        ))
        db.send_create_signal('base', ['Level'])

        # Adding model 'Sublevel'
        db.create_table('base_sublevel', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.IntegerField')()),
            ('level', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['base.Level'])),
        ))
        db.send_create_signal('base', ['Sublevel'])

        # Adding model 'Subject'
        db.create_table('base_subject', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('sublevel', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['base.Sublevel'])),
        ))
        db.send_create_signal('base', ['Subject'])

        # Adding model 'TutorProfile'
        db.create_table('base_tutorprofile', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
            ('dob', self.gf('django.db.models.fields.DateField')(null=True)),
            ('location', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['base.Location'], null=True)),
        ))
        db.send_create_signal('base', ['TutorProfile'])

        # Adding M2M table for field subjects_offered on 'TutorProfile'
        db.create_table('base_tutorprofile_subjects_offered', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('tutorprofile', models.ForeignKey(orm['base.tutorprofile'], null=False)),
            ('subject', models.ForeignKey(orm['base.subject'], null=False))
        ))
        db.create_unique('base_tutorprofile_subjects_offered', ['tutorprofile_id', 'subject_id'])


    def backwards(self, orm):
        
        # Deleting model 'State'
        db.delete_table('base_state')

        # Deleting model 'District'
        db.delete_table('base_district')

        # Deleting model 'Location'
        db.delete_table('base_location')

        # Deleting model 'Level'
        db.delete_table('base_level')

        # Deleting model 'Sublevel'
        db.delete_table('base_sublevel')

        # Deleting model 'Subject'
        db.delete_table('base_subject')

        # Deleting model 'TutorProfile'
        db.delete_table('base_tutorprofile')

        # Removing M2M table for field subjects_offered on 'TutorProfile'
        db.delete_table('base_tutorprofile_subjects_offered')


    models = {
        'auth.group': {
            'Meta': {'object_name': 'Group'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        'auth.permission': {
            'Meta': {'ordering': "('content_type__app_label', 'content_type__model', 'codename')", 'unique_together': "(('content_type', 'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        'base.district': {
            'Meta': {'object_name': 'District'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'state': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['base.State']"})
        },
        'base.level': {
            'Meta': {'object_name': 'Level'},
            'grade_name': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '20'})
        },
        'base.location': {
            'Meta': {'object_name': 'Location'},
            'district': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['base.District']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'base.state': {
            'Meta': {'object_name': 'State'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'base.subject': {
            'Meta': {'object_name': 'Subject'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'sublevel': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['base.Sublevel']"})
        },
        'base.sublevel': {
            'Meta': {'object_name': 'Sublevel'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'level': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['base.Level']"}),
            'name': ('django.db.models.fields.IntegerField', [], {})
        },
        'base.tutorprofile': {
            'Meta': {'object_name': 'TutorProfile'},
            'dob': ('django.db.models.fields.DateField', [], {'null': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'location': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['base.Location']", 'null': 'True'}),
            'subjects_offered': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['base.Subject']", 'symmetrical': 'False'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']"})
        },
        'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['base']
