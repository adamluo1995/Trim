# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils.encoding import python_2_unicode_compatible
# Create your models here.


@python_2_unicode_compatible
class Account(models.Model):
    email = models.EmailField(primary_key=True)
    password = models.CharField(max_length=20)
    nickname = models.CharField(max_length=20)

    def __str__(self):
        return self.email


@python_2_unicode_compatible
class Log(models.Model):
    account = models.ForeignKey('Account', on_delete=models.CASCADE)
    content = models.TextField(null=True)
    pub_time = models.DateTimeField(auto_now_add=True)
    # pub_time_sec = models.TimeField(auto_now_add=True)

    def __str__(self):
        return str(self.pub_time)


@python_2_unicode_compatible
class Blog(models.Model):
    account = models.ForeignKey('Account', on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    content = models.TextField(null=True)
    pub_time = models.DateTimeField(auto_now_add=True)
    # pub_time_sec = models.TimeField(auto_now_add=True)

    def __str__(self):
        return self.title


@python_2_unicode_compatible
class Goal(models.Model):
    account = models.ForeignKey('Account', on_delete=models.CASCADE)
    # id = models.AutoField(primary_key=False)
    title = models.CharField(max_length=50, default="No title")
    content = models.TextField(null=True, blank=True)
    pub_time = models.DateTimeField(auto_now_add=True)
    # pub_time_sec = models.TimeField(auto_now_add=True)
    records = models.CharField(max_length=1000, null=True, blank=True)
    is_active = models.BooleanField()

    def __str__(self):
        return self.title
