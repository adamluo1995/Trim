# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-30 23:12
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0011_auto_20170530_2304'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blog',
            name='pub_time_sec',
        ),
        migrations.RemoveField(
            model_name='goal',
            name='pub_time_sec',
        ),
        migrations.RemoveField(
            model_name='log',
            name='pub_time_sec',
        ),
    ]
