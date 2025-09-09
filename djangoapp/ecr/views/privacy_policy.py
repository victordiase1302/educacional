from django.shortcuts import render

def privacy_policy(request, *args, **kwargs):
    return render(request, 'ecr/privacy_policy.html')
