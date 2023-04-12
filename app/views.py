import os

from django.http import HttpResponse
from django.urls import reverse
from datetime import datetime


def hello_view(request):
    return HttpResponse('Функция: Hello')


def index_view(request):
    msg = "МЕНЮ:"

    msg += f'<br/><a href="{reverse("hello")}">hello</a>'
    msg += f'<br/><a href="{reverse("time")}">time_now</a>'
    msg += f'<br/><a href="{reverse("pwd")}">data</a>'

    return HttpResponse(msg)


def time_view(request):
    current_time = datetime.now()
    msg = f'Текущее время: {current_time}'
    return HttpResponse(msg)


def workdir_view(request):
    files = os.listdir(os.getcwd())
    return HttpResponse("<br/>".join(files))








