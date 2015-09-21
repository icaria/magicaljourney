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
                ('id', models.BigIntegerField(serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=50)),
                ('level', models.BigIntegerField()),
                ('is_online', models.BinaryField()),
                ('last_updated', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Division',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('description', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='League',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('description', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('message', models.CharField(max_length=1024)),
                ('date_time', models.DateTimeField()),
                ('account', models.ForeignKey(to='leaguebuddy.Account')),
            ],
        ),
        migrations.AddField(
            model_name='account',
            name='division',
            field=models.ForeignKey(to='leaguebuddy.Division'),
        ),
        migrations.AddField(
            model_name='account',
            name='league',
            field=models.ForeignKey(to='leaguebuddy.League'),
        ),
    ]
