from django.db import transaction
from django.http import HttpRequest, HttpResponse
from ecr.models import Lead
from django.shortcuts import render

# @require_POST
def create(request, *args, **kwargs):
    email = request.POST.get('email')
    try:
        with transaction.atomic():
            Lead.objects.create(email=email)
    except Exception as e:
        print(e)
    template_name = 'ecr/partials/congratulations_message.html'
    return render(request, template_name)
