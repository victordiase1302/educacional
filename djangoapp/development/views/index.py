from django.shortcuts import render


def index(request, *args, **kwargs):
    return render(request, 'development/profile.html')


def search(request, *args, **kwargs):
    return render(request, 'development/search.html')


def job_detail(request, *args, **kwargs):
    return render(request, 'development/job_detail.html')


def apply_form(request, *args, **kwargs):
    return render(request, 'development/apply_form.html')


def company_detail(request, *args, **kwargs):
    return render(request, 'development/company_detail.html')


def notification(request, *args, **kwargs):
    return render(request, 'development/notification.html')