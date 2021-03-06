# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Period'
        db.create_table('period', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('start', self.gf('django.db.models.fields.DateField')()),
            ('end', self.gf('django.db.models.fields.DateField')()),
            ('computed', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('needs_recompute', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('num_retplayers', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('num_newplayers', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('num_games', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('dom_p', self.gf('django.db.models.fields.FloatField')(null=True)),
            ('dom_t', self.gf('django.db.models.fields.FloatField')(null=True)),
            ('dom_z', self.gf('django.db.models.fields.FloatField')(null=True)),
        ))
        db.send_create_signal('ratings', ['Period'])

        # Adding model 'Event'
        db.create_table('event', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('parent', self.gf('django.db.models.fields.related.ForeignKey')(null=True, to=orm['ratings.Event'], blank=True)),
            ('lft', self.gf('django.db.models.fields.IntegerField')(db_index=True)),
            ('rgt', self.gf('django.db.models.fields.IntegerField')(db_index=True)),
            ('closed', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('big', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('noprint', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('fullname', self.gf('django.db.models.fields.CharField')(max_length=500, default='')),
            ('homepage', self.gf('django.db.models.fields.CharField')(null=True, blank=True, max_length=200)),
            ('lp_name', self.gf('django.db.models.fields.CharField')(null=True, blank=True, max_length=200)),
            ('tlpd_id', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('tlpd_db', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('tl_thread', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('prizepool', self.gf('django.db.models.fields.NullBooleanField')(null=True, blank=True)),
            ('earliest', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('latest', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('category', self.gf('django.db.models.fields.CharField')(null=True, blank=True, max_length=50)),
            ('type', self.gf('django.db.models.fields.CharField')(max_length=50)),
        ))
        db.send_create_signal('ratings', ['Event'])

        # Adding model 'Player'
        db.create_table('player', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('tag', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('name', self.gf('django.db.models.fields.CharField')(null=True, blank=True, db_index=True, max_length=100)),
            ('birthday', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('mcnum', self.gf('django.db.models.fields.IntegerField')(null=True, default=None, blank=True)),
            ('tlpd_id', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('tlpd_db', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('lp_name', self.gf('django.db.models.fields.CharField')(null=True, blank=True, max_length=200)),
            ('sc2c_id', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('sc2e_id', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('country', self.gf('django.db.models.fields.CharField')(null=True, blank=True, db_index=True, max_length=2)),
            ('race', self.gf('django.db.models.fields.CharField')(max_length=1, db_index=True)),
            ('dom_val', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('dom_start', self.gf('django.db.models.fields.related.ForeignKey')(null=True, related_name='player_dom_start', to=orm['ratings.Period'], blank=True)),
            ('dom_end', self.gf('django.db.models.fields.related.ForeignKey')(null=True, related_name='player_dom_end', to=orm['ratings.Period'], blank=True)),
        ))
        db.send_create_signal('ratings', ['Player'])

        # Adding model 'Story'
        db.create_table('story', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('player', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['ratings.Player'])),
            ('text', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('date', self.gf('django.db.models.fields.DateField')()),
            ('event', self.gf('django.db.models.fields.related.ForeignKey')(null=True, to=orm['ratings.Event'])),
        ))
        db.send_create_signal('ratings', ['Story'])

        # Adding model 'Group'
        db.create_table('group', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100, db_index=True)),
            ('shortname', self.gf('django.db.models.fields.CharField')(null=True, blank=True, max_length=25)),
            ('scoreak', self.gf('django.db.models.fields.FloatField')(null=True, default=0.0)),
            ('scorepl', self.gf('django.db.models.fields.FloatField')(null=True, default=0.0)),
            ('founded', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('disbanded', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('active', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('homepage', self.gf('django.db.models.fields.CharField')(null=True, blank=True, max_length=200)),
            ('lp_name', self.gf('django.db.models.fields.CharField')(null=True, blank=True, max_length=200)),
            ('is_team', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('is_manual', self.gf('django.db.models.fields.BooleanField')(default=True)),
        ))
        db.send_create_signal('ratings', ['Group'])

        # Adding model 'GroupMembership'
        db.create_table('groupmembership', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('player', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['ratings.Player'])),
            ('group', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['ratings.Group'])),
            ('start', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('end', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('current', self.gf('django.db.models.fields.BooleanField')(default=True, db_index=True)),
            ('playing', self.gf('django.db.models.fields.BooleanField')(default=True, db_index=True)),
        ))
        db.send_create_signal('ratings', ['GroupMembership'])

        # Adding model 'Alias'
        db.create_table('alias', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('player', self.gf('django.db.models.fields.related.ForeignKey')(null=True, to=orm['ratings.Player'])),
            ('group', self.gf('django.db.models.fields.related.ForeignKey')(null=True, to=orm['ratings.Group'])),
        ))
        db.send_create_signal('ratings', ['Alias'])

        # Adding model 'Match'
        db.create_table('match', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('period', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['ratings.Period'])),
            ('date', self.gf('django.db.models.fields.DateField')()),
            ('pla', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['ratings.Player'], related_name='match_pla')),
            ('plb', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['ratings.Player'], related_name='match_plb')),
            ('sca', self.gf('django.db.models.fields.SmallIntegerField')(db_index=True)),
            ('scb', self.gf('django.db.models.fields.SmallIntegerField')(db_index=True)),
            ('rca', self.gf('django.db.models.fields.CharField')(max_length=1, db_index=True)),
            ('rcb', self.gf('django.db.models.fields.CharField')(max_length=1, db_index=True)),
            ('treated', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('event', self.gf('django.db.models.fields.CharField')(max_length=200, default='', blank=True)),
            ('eventobj', self.gf('django.db.models.fields.related.ForeignKey')(null=True, to=orm['ratings.Event'], blank=True)),
            ('submitter', self.gf('django.db.models.fields.related.ForeignKey')(null=True, to=orm['auth.User'], blank=True)),
            ('game', self.gf('django.db.models.fields.CharField')(max_length=10, default='WoL', db_index=True)),
            ('offline', self.gf('django.db.models.fields.BooleanField')(default=False, db_index=True)),
            ('rta', self.gf('django.db.models.fields.related.ForeignKey')(null=True, related_name='rta', to=orm['ratings.Rating'])),
            ('rtb', self.gf('django.db.models.fields.related.ForeignKey')(null=True, related_name='rtb', to=orm['ratings.Rating'])),
        ))
        db.send_create_signal('ratings', ['Match'])

        # Adding model 'Message'
        db.create_table('message', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('type', self.gf('django.db.models.fields.CharField')(max_length=10)),
            ('title', self.gf('django.db.models.fields.CharField')(null=True, max_length=100)),
            ('text', self.gf('django.db.models.fields.TextField')()),
            ('player', self.gf('django.db.models.fields.related.ForeignKey')(null=True, to=orm['ratings.Player'])),
            ('event', self.gf('django.db.models.fields.related.ForeignKey')(null=True, to=orm['ratings.Event'])),
            ('group', self.gf('django.db.models.fields.related.ForeignKey')(null=True, to=orm['ratings.Group'])),
            ('match', self.gf('django.db.models.fields.related.ForeignKey')(null=True, to=orm['ratings.Match'])),
        ))
        db.send_create_signal('ratings', ['Message'])

        # Adding model 'Earnings'
        db.create_table('earnings', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('event', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['ratings.Event'])),
            ('player', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['ratings.Player'])),
            ('earnings', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('origearnings', self.gf('django.db.models.fields.IntegerField')()),
            ('currency', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('placement', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal('ratings', ['Earnings'])

        # Adding model 'PreMatchGroup'
        db.create_table('prematchgroup', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('date', self.gf('django.db.models.fields.DateField')()),
            ('event', self.gf('django.db.models.fields.CharField')(max_length=200, default='', blank=True)),
            ('source', self.gf('django.db.models.fields.CharField')(null=True, default='', blank=True, max_length=500)),
            ('contact', self.gf('django.db.models.fields.CharField')(null=True, default='', blank=True, max_length=200)),
            ('notes', self.gf('django.db.models.fields.TextField')(null=True, default='', blank=True)),
            ('game', self.gf('django.db.models.fields.CharField')(max_length=10, default='wol')),
            ('offline', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal('ratings', ['PreMatchGroup'])

        # Adding model 'PreMatch'
        db.create_table('prematch', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('group', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['ratings.PreMatchGroup'])),
            ('pla', self.gf('django.db.models.fields.related.ForeignKey')(null=True, related_name='prematch_pla', to=orm['ratings.Player'], blank=True)),
            ('plb', self.gf('django.db.models.fields.related.ForeignKey')(null=True, related_name='prematch_plb', to=orm['ratings.Player'], blank=True)),
            ('pla_string', self.gf('django.db.models.fields.CharField')(null=True, default='', blank=True, max_length=200)),
            ('plb_string', self.gf('django.db.models.fields.CharField')(null=True, default='', blank=True, max_length=200)),
            ('sca', self.gf('django.db.models.fields.SmallIntegerField')()),
            ('scb', self.gf('django.db.models.fields.SmallIntegerField')()),
            ('date', self.gf('django.db.models.fields.DateField')()),
            ('rca', self.gf('django.db.models.fields.CharField')(null=True, max_length=1)),
            ('rcb', self.gf('django.db.models.fields.CharField')(null=True, max_length=1)),
        ))
        db.send_create_signal('ratings', ['PreMatch'])

        # Adding model 'Rating'
        db.create_table('rating', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('period', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['ratings.Period'])),
            ('player', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['ratings.Player'])),
            ('prev', self.gf('django.db.models.fields.related.ForeignKey')(null=True, related_name='prevrating', to=orm['ratings.Rating'])),
            ('rating', self.gf('django.db.models.fields.FloatField')()),
            ('rating_vp', self.gf('django.db.models.fields.FloatField')()),
            ('rating_vt', self.gf('django.db.models.fields.FloatField')()),
            ('rating_vz', self.gf('django.db.models.fields.FloatField')()),
            ('dev', self.gf('django.db.models.fields.FloatField')()),
            ('dev_vp', self.gf('django.db.models.fields.FloatField')()),
            ('dev_vt', self.gf('django.db.models.fields.FloatField')()),
            ('dev_vz', self.gf('django.db.models.fields.FloatField')()),
            ('comp_rat', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('comp_rat_vp', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('comp_rat_vt', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('comp_rat_vz', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('comp_dev', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('comp_dev_vp', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('comp_dev_vt', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('comp_dev_vz', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('bf_rating', self.gf('django.db.models.fields.FloatField')(default=0)),
            ('bf_rating_vp', self.gf('django.db.models.fields.FloatField')(default=0)),
            ('bf_rating_vt', self.gf('django.db.models.fields.FloatField')(default=0)),
            ('bf_rating_vz', self.gf('django.db.models.fields.FloatField')(default=0)),
            ('bf_dev', self.gf('django.db.models.fields.FloatField')(null=True, default=1, blank=True)),
            ('bf_dev_vp', self.gf('django.db.models.fields.FloatField')(null=True, default=1, blank=True)),
            ('bf_dev_vt', self.gf('django.db.models.fields.FloatField')(null=True, default=1, blank=True)),
            ('bf_dev_vz', self.gf('django.db.models.fields.FloatField')(null=True, default=1, blank=True)),
            ('position', self.gf('django.db.models.fields.IntegerField')(null=True)),
            ('position_vp', self.gf('django.db.models.fields.IntegerField')(null=True)),
            ('position_vt', self.gf('django.db.models.fields.IntegerField')(null=True)),
            ('position_vz', self.gf('django.db.models.fields.IntegerField')(null=True)),
            ('decay', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('domination', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
        ))
        db.send_create_signal('ratings', ['Rating'])

        # Adding model 'BalanceEntry'
        db.create_table('balanceentry', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('date', self.gf('django.db.models.fields.DateField')()),
            ('pvt_wins', self.gf('django.db.models.fields.IntegerField')()),
            ('pvt_losses', self.gf('django.db.models.fields.IntegerField')()),
            ('pvz_wins', self.gf('django.db.models.fields.IntegerField')()),
            ('pvz_losses', self.gf('django.db.models.fields.IntegerField')()),
            ('tvz_wins', self.gf('django.db.models.fields.IntegerField')()),
            ('tvz_losses', self.gf('django.db.models.fields.IntegerField')()),
            ('p_gains', self.gf('django.db.models.fields.FloatField')()),
            ('t_gains', self.gf('django.db.models.fields.FloatField')()),
            ('z_gains', self.gf('django.db.models.fields.FloatField')()),
        ))
        db.send_create_signal('ratings', ['BalanceEntry'])


    def backwards(self, orm):
        # Deleting model 'Period'
        db.delete_table('period')

        # Deleting model 'Event'
        db.delete_table('event')

        # Deleting model 'Player'
        db.delete_table('player')

        # Deleting model 'Story'
        db.delete_table('story')

        # Deleting model 'Group'
        db.delete_table('group')

        # Deleting model 'GroupMembership'
        db.delete_table('groupmembership')

        # Deleting model 'Alias'
        db.delete_table('alias')

        # Deleting model 'Match'
        db.delete_table('match')

        # Deleting model 'Message'
        db.delete_table('message')

        # Deleting model 'Earnings'
        db.delete_table('earnings')

        # Deleting model 'PreMatchGroup'
        db.delete_table('prematchgroup')

        # Deleting model 'PreMatch'
        db.delete_table('prematch')

        # Deleting model 'Rating'
        db.delete_table('rating')

        # Deleting model 'BalanceEntry'
        db.delete_table('balanceentry')


    models = {
        'auth.group': {
            'Meta': {'object_name': 'Group'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '80', 'unique': 'True'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        'auth.permission': {
            'Meta': {'object_name': 'Permission', 'ordering': "('content_type__app_label', 'content_type__model', 'codename')", 'unique_together': "(('content_type', 'codename'),)"},
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
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'user_set'", 'symmetrical': 'False', 'to': "orm['auth.Group']", 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'user_set'", 'symmetrical': 'False', 'to': "orm['auth.Permission']", 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'max_length': '30', 'unique': 'True'})
        },
        'contenttypes.contenttype': {
            'Meta': {'object_name': 'ContentType', 'db_table': "'django_content_type'", 'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'ratings.alias': {
            'Meta': {'object_name': 'Alias', 'db_table': "'alias'"},
            'group': ('django.db.models.fields.related.ForeignKey', [], {'null': 'True', 'to': "orm['ratings.Group']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'player': ('django.db.models.fields.related.ForeignKey', [], {'null': 'True', 'to': "orm['ratings.Player']"})
        },
        'ratings.balanceentry': {
            'Meta': {'object_name': 'BalanceEntry', 'db_table': "'balanceentry'"},
            'date': ('django.db.models.fields.DateField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'p_gains': ('django.db.models.fields.FloatField', [], {}),
            'pvt_losses': ('django.db.models.fields.IntegerField', [], {}),
            'pvt_wins': ('django.db.models.fields.IntegerField', [], {}),
            'pvz_losses': ('django.db.models.fields.IntegerField', [], {}),
            'pvz_wins': ('django.db.models.fields.IntegerField', [], {}),
            't_gains': ('django.db.models.fields.FloatField', [], {}),
            'tvz_losses': ('django.db.models.fields.IntegerField', [], {}),
            'tvz_wins': ('django.db.models.fields.IntegerField', [], {}),
            'z_gains': ('django.db.models.fields.FloatField', [], {})
        },
        'ratings.earnings': {
            'Meta': {'object_name': 'Earnings', 'db_table': "'earnings'"},
            'currency': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'earnings': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'event': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['ratings.Event']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'origearnings': ('django.db.models.fields.IntegerField', [], {}),
            'placement': ('django.db.models.fields.IntegerField', [], {}),
            'player': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['ratings.Player']"})
        },
        'ratings.event': {
            'Meta': {'object_name': 'Event', 'db_table': "'event'", 'ordering': "['lft']"},
            'big': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'category': ('django.db.models.fields.CharField', [], {'null': 'True', 'blank': 'True', 'max_length': '50'}),
            'closed': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'earliest': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'fullname': ('django.db.models.fields.CharField', [], {'max_length': '500', 'default': "''"}),
            'homepage': ('django.db.models.fields.CharField', [], {'null': 'True', 'blank': 'True', 'max_length': '200'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'latest': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'lft': ('django.db.models.fields.IntegerField', [], {'db_index': 'True'}),
            'lp_name': ('django.db.models.fields.CharField', [], {'null': 'True', 'blank': 'True', 'max_length': '200'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'noprint': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'parent': ('django.db.models.fields.related.ForeignKey', [], {'null': 'True', 'to': "orm['ratings.Event']", 'blank': 'True'}),
            'prizepool': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'rgt': ('django.db.models.fields.IntegerField', [], {'db_index': 'True'}),
            'tl_thread': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'tlpd_db': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'tlpd_id': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'type': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'ratings.group': {
            'Meta': {'object_name': 'Group', 'db_table': "'group'"},
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'disbanded': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'founded': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'homepage': ('django.db.models.fields.CharField', [], {'null': 'True', 'blank': 'True', 'max_length': '200'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_manual': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_team': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'lp_name': ('django.db.models.fields.CharField', [], {'null': 'True', 'blank': 'True', 'max_length': '200'}),
            'members': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['ratings.Player']", 'symmetrical': 'False', 'through': "orm['ratings.GroupMembership']"}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_index': 'True'}),
            'scoreak': ('django.db.models.fields.FloatField', [], {'null': 'True', 'default': '0.0'}),
            'scorepl': ('django.db.models.fields.FloatField', [], {'null': 'True', 'default': '0.0'}),
            'shortname': ('django.db.models.fields.CharField', [], {'null': 'True', 'blank': 'True', 'max_length': '25'})
        },
        'ratings.groupmembership': {
            'Meta': {'object_name': 'GroupMembership', 'db_table': "'groupmembership'"},
            'current': ('django.db.models.fields.BooleanField', [], {'default': 'True', 'db_index': 'True'}),
            'end': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'group': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['ratings.Group']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'player': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['ratings.Player']"}),
            'playing': ('django.db.models.fields.BooleanField', [], {'default': 'True', 'db_index': 'True'}),
            'start': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'})
        },
        'ratings.match': {
            'Meta': {'object_name': 'Match', 'db_table': "'match'"},
            'date': ('django.db.models.fields.DateField', [], {}),
            'event': ('django.db.models.fields.CharField', [], {'max_length': '200', 'default': "''", 'blank': 'True'}),
            'eventobj': ('django.db.models.fields.related.ForeignKey', [], {'null': 'True', 'to': "orm['ratings.Event']", 'blank': 'True'}),
            'game': ('django.db.models.fields.CharField', [], {'max_length': '10', 'default': "'WoL'", 'db_index': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'offline': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'db_index': 'True'}),
            'period': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['ratings.Period']"}),
            'pla': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['ratings.Player']", 'related_name': "'match_pla'"}),
            'plb': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['ratings.Player']", 'related_name': "'match_plb'"}),
            'rca': ('django.db.models.fields.CharField', [], {'max_length': '1', 'db_index': 'True'}),
            'rcb': ('django.db.models.fields.CharField', [], {'max_length': '1', 'db_index': 'True'}),
            'rta': ('django.db.models.fields.related.ForeignKey', [], {'null': 'True', 'related_name': "'rta'", 'to': "orm['ratings.Rating']"}),
            'rtb': ('django.db.models.fields.related.ForeignKey', [], {'null': 'True', 'related_name': "'rtb'", 'to': "orm['ratings.Rating']"}),
            'sca': ('django.db.models.fields.SmallIntegerField', [], {'db_index': 'True'}),
            'scb': ('django.db.models.fields.SmallIntegerField', [], {'db_index': 'True'}),
            'submitter': ('django.db.models.fields.related.ForeignKey', [], {'null': 'True', 'to': "orm['auth.User']", 'blank': 'True'}),
            'treated': ('django.db.models.fields.BooleanField', [], {'default': 'False'})
        },
        'ratings.message': {
            'Meta': {'object_name': 'Message', 'db_table': "'message'"},
            'event': ('django.db.models.fields.related.ForeignKey', [], {'null': 'True', 'to': "orm['ratings.Event']"}),
            'group': ('django.db.models.fields.related.ForeignKey', [], {'null': 'True', 'to': "orm['ratings.Group']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'match': ('django.db.models.fields.related.ForeignKey', [], {'null': 'True', 'to': "orm['ratings.Match']"}),
            'player': ('django.db.models.fields.related.ForeignKey', [], {'null': 'True', 'to': "orm['ratings.Player']"}),
            'text': ('django.db.models.fields.TextField', [], {}),
            'title': ('django.db.models.fields.CharField', [], {'null': 'True', 'max_length': '100'}),
            'type': ('django.db.models.fields.CharField', [], {'max_length': '10'})
        },
        'ratings.period': {
            'Meta': {'object_name': 'Period', 'db_table': "'period'"},
            'computed': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'dom_p': ('django.db.models.fields.FloatField', [], {'null': 'True'}),
            'dom_t': ('django.db.models.fields.FloatField', [], {'null': 'True'}),
            'dom_z': ('django.db.models.fields.FloatField', [], {'null': 'True'}),
            'end': ('django.db.models.fields.DateField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'needs_recompute': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'num_games': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'num_newplayers': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'num_retplayers': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'start': ('django.db.models.fields.DateField', [], {})
        },
        'ratings.player': {
            'Meta': {'object_name': 'Player', 'db_table': "'player'", 'ordering': "['tag']"},
            'birthday': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'country': ('django.db.models.fields.CharField', [], {'null': 'True', 'blank': 'True', 'db_index': 'True', 'max_length': '2'}),
            'dom_end': ('django.db.models.fields.related.ForeignKey', [], {'null': 'True', 'related_name': "'player_dom_end'", 'to': "orm['ratings.Period']", 'blank': 'True'}),
            'dom_start': ('django.db.models.fields.related.ForeignKey', [], {'null': 'True', 'related_name': "'player_dom_start'", 'to': "orm['ratings.Period']", 'blank': 'True'}),
            'dom_val': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lp_name': ('django.db.models.fields.CharField', [], {'null': 'True', 'blank': 'True', 'max_length': '200'}),
            'mcnum': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'default': 'None', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'null': 'True', 'blank': 'True', 'db_index': 'True', 'max_length': '100'}),
            'race': ('django.db.models.fields.CharField', [], {'max_length': '1', 'db_index': 'True'}),
            'sc2c_id': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'sc2e_id': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'tag': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'tlpd_db': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'tlpd_id': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'})
        },
        'ratings.prematch': {
            'Meta': {'object_name': 'PreMatch', 'db_table': "'prematch'"},
            'date': ('django.db.models.fields.DateField', [], {}),
            'group': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['ratings.PreMatchGroup']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'pla': ('django.db.models.fields.related.ForeignKey', [], {'null': 'True', 'related_name': "'prematch_pla'", 'to': "orm['ratings.Player']", 'blank': 'True'}),
            'pla_string': ('django.db.models.fields.CharField', [], {'null': 'True', 'default': "''", 'blank': 'True', 'max_length': '200'}),
            'plb': ('django.db.models.fields.related.ForeignKey', [], {'null': 'True', 'related_name': "'prematch_plb'", 'to': "orm['ratings.Player']", 'blank': 'True'}),
            'plb_string': ('django.db.models.fields.CharField', [], {'null': 'True', 'default': "''", 'blank': 'True', 'max_length': '200'}),
            'rca': ('django.db.models.fields.CharField', [], {'null': 'True', 'max_length': '1'}),
            'rcb': ('django.db.models.fields.CharField', [], {'null': 'True', 'max_length': '1'}),
            'sca': ('django.db.models.fields.SmallIntegerField', [], {}),
            'scb': ('django.db.models.fields.SmallIntegerField', [], {})
        },
        'ratings.prematchgroup': {
            'Meta': {'object_name': 'PreMatchGroup', 'db_table': "'prematchgroup'"},
            'contact': ('django.db.models.fields.CharField', [], {'null': 'True', 'default': "''", 'blank': 'True', 'max_length': '200'}),
            'date': ('django.db.models.fields.DateField', [], {}),
            'event': ('django.db.models.fields.CharField', [], {'max_length': '200', 'default': "''", 'blank': 'True'}),
            'game': ('django.db.models.fields.CharField', [], {'max_length': '10', 'default': "'wol'"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'notes': ('django.db.models.fields.TextField', [], {'null': 'True', 'default': "''", 'blank': 'True'}),
            'offline': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'source': ('django.db.models.fields.CharField', [], {'null': 'True', 'default': "''", 'blank': 'True', 'max_length': '500'})
        },
        'ratings.rating': {
            'Meta': {'object_name': 'Rating', 'db_table': "'rating'", 'ordering': "['period']"},
            'bf_dev': ('django.db.models.fields.FloatField', [], {'null': 'True', 'default': '1', 'blank': 'True'}),
            'bf_dev_vp': ('django.db.models.fields.FloatField', [], {'null': 'True', 'default': '1', 'blank': 'True'}),
            'bf_dev_vt': ('django.db.models.fields.FloatField', [], {'null': 'True', 'default': '1', 'blank': 'True'}),
            'bf_dev_vz': ('django.db.models.fields.FloatField', [], {'null': 'True', 'default': '1', 'blank': 'True'}),
            'bf_rating': ('django.db.models.fields.FloatField', [], {'default': '0'}),
            'bf_rating_vp': ('django.db.models.fields.FloatField', [], {'default': '0'}),
            'bf_rating_vt': ('django.db.models.fields.FloatField', [], {'default': '0'}),
            'bf_rating_vz': ('django.db.models.fields.FloatField', [], {'default': '0'}),
            'comp_dev': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'comp_dev_vp': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'comp_dev_vt': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'comp_dev_vz': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'comp_rat': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'comp_rat_vp': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'comp_rat_vt': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'comp_rat_vz': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'decay': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'dev': ('django.db.models.fields.FloatField', [], {}),
            'dev_vp': ('django.db.models.fields.FloatField', [], {}),
            'dev_vt': ('django.db.models.fields.FloatField', [], {}),
            'dev_vz': ('django.db.models.fields.FloatField', [], {}),
            'domination': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'period': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['ratings.Period']"}),
            'player': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['ratings.Player']"}),
            'position': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'position_vp': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'position_vt': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'position_vz': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'prev': ('django.db.models.fields.related.ForeignKey', [], {'null': 'True', 'related_name': "'prevrating'", 'to': "orm['ratings.Rating']"}),
            'rating': ('django.db.models.fields.FloatField', [], {}),
            'rating_vp': ('django.db.models.fields.FloatField', [], {}),
            'rating_vt': ('django.db.models.fields.FloatField', [], {}),
            'rating_vz': ('django.db.models.fields.FloatField', [], {})
        },
        'ratings.story': {
            'Meta': {'object_name': 'Story', 'db_table': "'story'"},
            'date': ('django.db.models.fields.DateField', [], {}),
            'event': ('django.db.models.fields.related.ForeignKey', [], {'null': 'True', 'to': "orm['ratings.Event']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'player': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['ratings.Player']"}),
            'text': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        }
    }

    complete_apps = ['ratings']