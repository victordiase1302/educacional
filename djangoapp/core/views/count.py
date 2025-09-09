from django.http import HttpResponse
from django.db import transaction
from counters.models import Visit


def count(request):    
    pwa = string_to_bool(request.POST.get('isPWA'))
    is_mobile = string_to_bool(request.POST.get('isMobile'))
    isIphone = string_to_bool(request.POST.get('isIphone'))
    referer = request.POST.get('referer')    
    if user_ip := request.META.get('HTTP_X_FORWARDED_FOR'):
        ip_address = user_ip.split(',')[0]
    else:
        ip_address = request.META.get('REMOTE_ADDR')
    user_agent = request.META.get('HTTP_USER_AGENT')    
    
    is_mobile = 'Mobile' in user_agent
    try:
        with transaction.atomic():
            Visit.objects.create(
                ip_address=ip_address,
                is_mobile=is_mobile,
                referer=referer,
                is_pwa=pwa,
                is_iphone=isIphone,
            )
    except Exception as e:
        print(e)

    return HttpResponse(status=201)


def string_to_bool(value):
    return value.lower() == 'true'