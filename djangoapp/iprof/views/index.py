from django.http import JsonResponse
from django.shortcuts import render


def index_view(request):
    template_name = "iprof/index.html"
    return render(request, template_name)
