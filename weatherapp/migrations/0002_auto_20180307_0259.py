# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-03-07 02:59
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('weatherapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='reading',
            old_name='preip',
            new_name='precip',
        ),
    ]
