# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-03-06 06:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Reading',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location', models.CharField(max_length=100)),
                ('weather', models.CharField(max_length=20)),
                ('wind_str', models.CharField(max_length=100)),
                ('temp', models.IntegerField()),
                ('humidity', models.CharField(max_length=10)),
                ('preip', models.CharField(max_length=50)),
                ('icon_url', models.URLField()),
                ('observation_time', models.CharField(max_length=100)),
            ],
        ),
    ]
