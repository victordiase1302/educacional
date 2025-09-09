from django.core.cache import cache
from django.shortcuts import render


def request_otp(request, *args, **kwargs):
    if request.method == "GET":
        phone_number = kwargs.get('phone_number')
        otp = 'otp'
        cache.set(f"+55{phone_number}", otp, 60 * 15)
