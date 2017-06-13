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
    if request.session.get('remember_me', False) and request.session.get('email'):
        return HttpResponseRedirect(reverse('login:signin'))
    else:
        return render(request, 'login/index.html')


def home(request):
    account = models.Account.objects.get(pk=request.session['email'])
    return render(request, 'login/home.html', {'account': account})


def signin(request):
    if request.session.get('email'):
        pass
    else:
        account = models.Account.objects.get(pk=request.POST['email'])
        request.session['email'] = account.email
        if request.POST.get('remember', False):
            request.session['remember_me'] = True
    # return render(request, 'login/home.html', {'account': account})
    return HttpResponseRedirect(reverse('login:home'))


def signup(request):
    email = request.POST['email']
    pwd = request.POST['pwd']
    nickname = request.POST['nickname']
    models.Account.objects.create(email=email, password=pwd, nickname=nickname)
    return HttpResponseRedirect(reverse('login:signin'))

@csrf_exempt
def check_email(request):
    email = request.POST['email']
    try:
        models.Account.objects.get(pk=email)
    except ObjectDoesNotExist:
        return JsonResponse({'email': '0'})
    else:
        return JsonResponse({'email': '1'})


@csrf_exempt
def check_signin(request):
    account = models.Account.objects.filter(pk=request.POST['email'])
    if account:
        account = models.Account.objects.get(pk=request.POST['email'])
        if account.password == request.POST['pwd']:
            return JsonResponse({'error': '0'})
        else:
            print('error', 1)
            return JsonResponse({'error': '1'})
    else:
        return JsonResponse({'error': '2'})


@csrf_exempt
def add_log(request):
    account = models.Account.objects.get(pk=request.session['email'])
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

    # return render_to_response('login/home.html', {'account': account})
    return HttpResponseRedirect(reverse('login:home'))

@csrf_exempt
def goal_edit(request):
    account = models.Account.objects.get(pk=request.session['email'])
    if request.POST['id'] == '0':
        models.Goal.objects.create(account=account, title=request.POST['title'], content=request.POST['content'],
                                   is_active=True)
    else:
        goal = models.Goal.objects.get(pk=request.POST['id'])
        goal.content = request.POST['content']
        goal.title = request.POST['title']
        goal.save()

    # return render_to_response('login/home.html', {'account': account})
    return HttpResponseRedirect(reverse('login:home'))


def close(request):
    if not request.session.get('remember_me', False):
        if request.session.get('email'):
            del request.session['email']
    return JsonResponse(dict())


def signout(request):
    if request.session.get('remember_me', False):
        del request.session['remember_me']
    if request.session.get('email'):
        del request.session['email']
    return HttpResponseRedirect(reverse('login:index'))
