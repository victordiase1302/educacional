import threading

from counters.views import increment_counter, service_counter
from django.conf import settings
from django.contrib.auth import login
from django.shortcuts import render
from users.forms import LoginForm


def about(request, *args, **kwargs):
    if request.method == 'GET':

        return render(request, 'core/base_link_tree.html')


