# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, render_to_response
from . import models
from django.core.exceptions import ObjectDoesNotExist
from django.http import JsonResponse, HttpResponseRedirect
from django.urls import reverse
from django.template import RequestContext
from django.views.decorators.csrf import csrf_exempt

# Create your views here.


def index(request):
    print('remote request: ', request.META['REMOTE_ADDR'])
    if 'email' in request.COOKIES and 'password'in request.COOKIES:
        account = models.Account.objects.get(pk=request.COOKIES['email'])
        response = render_to_response('login/home.html', {"account": account})
        return response
    else:
        return render(request, 'login/index.html')


def signin(request):
    account = models.Account.objects.get(pk=request.POST['email'])
    response = render_to_response('login/home.html', {"account": account})
    if request.POST['remember']:
        response.set_cookie('email', account.email)
        response.set_cookie('password', account.password)
    return response


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


@csrf_exempt
def add_log(request):
    account = models.Account.objects.get(pk=request.COOKIES['email'])
    # print(request.POST)
    # assert False
    models.Log.objects.create(account=account, content=request.POST['_log_message'])
    goals = account.goal_set.all()
    for goal in goals:
        if goal.records:
            goal.records = goal.records + request.POST['_goal_score_' + str(goal.id)]
        else:
            goal.records = request.POST['_goal_score_' + str(goal.id)]
        goal.save()

    return render_to_response('login/home.html', {'account': account})

@csrf_exempt
def goal_edit(request):
    account = models.Account.objects.get(pk=request.POST['email'])
    if request.POST['id'] == '0':
        models.Goal.objects.create(account=account, title=request.POST['title'], content=request.POST['content'],
                                   is_active=True)
    else:
        goal = models.Goal.objects.get(pk=request.POST['id'])
        goal.content = request.POST['content']
        goal.title = request.POST['title']
        goal.save()

    return render_to_response('login/home.html', {'account': account})
