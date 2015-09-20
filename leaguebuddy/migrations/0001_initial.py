# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('AccountId', models.BigIntegerField()),
                ('Name', models.CharField(max_length=50)),
                ('IsOnline', models.BinaryField()),
                ('InGame', models.BinaryField()),
            ],
        ),
        migrations.CreateModel(
            name='Division',
            fields=[
                ('DivisionId', models.AutoField(serialize=False, primary_key=True)),
                ('Description', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='League',
            fields=[
                ('LeagueId', models.AutoField(serialize=False, primary_key=True)),
                ('Description', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('NotificationId', models.AutoField(serialize=False, primary_key=True)),
                ('Message', models.CharField(max_length=1024)),
                ('DateTime', models.DateTimeField()),
                ('AccountId', models.ForeignKey(to='leaguebuddy.Account')),
            ],
        ),
        migrations.AddField(
            model_name='account',
            name='DivisionId',
            field=models.ForeignKey(to='leaguebuddy.Division'),
        ),
        migrations.AddField(
            model_name='account',
            name='LeagueId',
            field=models.ForeignKey(to='leaguebuddy.League'),
        ),
    ]
