# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-23 11:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0002_auto_20170523_1048'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='account',
            name='id',
        ),
        migrations.AlterField(
            model_name='account',
            name='email',
            field=models.EmailField(max_length=254, primary_key=True, serialize=False),
        ),
    ]
