# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.


class Account(models.Model):
    email = models.EmailField(primary_key=True)
    password = models.CharField(max_length=20)
    nickname = models.CharField(max_length=20)

    def __str__(self):
        return self.email


class Log(models.Model):
    account = models.ForeignKey('Account', on_delete=models.CASCADE)
    content = models.TextField(null=True)
    pub_date = models.DateField(auto_now=True)

    def __str__(self):
        return self.pub_date


class Blog(models.Model):
    account = models.ForeignKey('Account', on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    content = models.TextField(null=True)
    pub_date = models.DateField(auto_now=True)

    def __str__(self):
        return self.title


class Goal(models.Model):
    account = models.ForeignKey('Account', on_delete=models.CASCADE)
    content = models.CharField(max_length=50)
    pub_date = models.DateField(auto_now=True)
    records = models.CharField(max_length=1000)
    is_active = models.BooleanField()

    def __str__(self):
        return self.content
