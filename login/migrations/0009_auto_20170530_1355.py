# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-30 13:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0008_auto_20170530_0854'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blog',
            name='pub_date',
        ),
        migrations.RemoveField(
            model_name='goal',
            name='pub_date',
        ),
        migrations.RemoveField(
            model_name='log',
            name='pub_date',
        ),
        migrations.AddField(
            model_name='blog',
            name='pub_time',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='goal',
            name='pub_time',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='log',
            name='pub_time',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
