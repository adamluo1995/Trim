# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from models import Account, Log, Blog, Goal

# Register your models here.


class AccountAdmin(admin.ModelAdmin):
    list_display = ('email', 'nickname')


class LogAdmin(admin.ModelAdmin):
    list_display = ('content', 'pub_time', 'id')


class BlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'pub_time', 'id')


class GoalAdmin(admin.ModelAdmin):
    list_display = ('title', 'pub_time', 'id')

admin.site.register(Account, AccountAdmin)
admin.site.register(Log, LogAdmin)
admin.site.register(Blog, BlogAdmin)
admin.site.register(Goal, GoalAdmin)




