# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-30 08:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0006_auto_20170528_0854'),
    ]

    operations = [
        migrations.AlterField(
            model_name='goal',
            name='records',
            field=models.CharField(max_length=1000, null=True),
        ),
    ]
