# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from . import models
from django.core.exceptions import ObjectDoesNotExist
from django.http import JsonResponse

# Create your views here.


def index(request):
    return render(request, 'login/index.html')


def signin(request):
    account = models.Account.objects.get(pk=request.POST['email'])
    return render(request, 'login/home.html', {'account': account})


def signup(request):
    email = request.POST['email']
    pwd = request.POST['pwd']
    nickname = request.POST['nickname']
    models.Account.objects.create(email=email, password=pwd, nickname=nickname)

    return render(request, 'login/index.html')


def check_email(request):

    email = request.GET['email']
    try:
        models.Account.objects.get(pk=email)
    except ObjectDoesNotExist:
        return JsonResponse({'email': '0'})
    else:
        return JsonResponse({'email': '1'})

    # try:
    #     models.Account.objects.get(pk=email)
    # except ObjectDoesNotExist:
    #     return '0'
    # else:
    #     return '1'
