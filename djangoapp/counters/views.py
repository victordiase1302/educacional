from django.db import transaction
from django.http import HttpRequest, HttpResponse

from .models import Services, Visit

# from django.views.decorators.http import require_POST


def increment_counter(request: HttpRequest):
    if user_ip := request.META.get('HTTP_X_FORWARDED_FOR'):
        ip_address = user_ip.split(',')[0]
    else:
        ip_address = request.META.get('REMOTE_ADDR')
    user_agent = request.META.get('HTTP_USER_AGENT')
    referer = (
            request.GET.get('ref') or request.META.get('HTTP_REFERER')
        ) or 'https://danielfortune.com.br/'
    if referer == 'https://danielfortune.com.br/serviceworker.js':
        referer = 'DanielFortune APP'
    is_mobile = 'Mobile' in user_agent
    try:
        with transaction.atomic():
            # if Visit.objects.exists():
            #     visit = Visit.objects.first()
            #     visit.counter += 1
            #     visit.save()
            # else:
            #     visit = Visit.objects.create(counter=1)

            Visit.objects.create(
                ip_address=ip_address,
                is_mobile=is_mobile,
                referer=referer
            )
    except Exception as e:
        print(e)

    return None


# @require_POST
def service_counter(request, *args, **kwargs):
    service = request.POST.get('service')
    if kwargs.get('user'):
        service = f"{service} - {kwargs.get('user')}"
    if kwargs.get('q'):
        service = f"Pesquisou pelo termo - {kwargs.get('q')}"
    if kwargs.get('search_term'):
        service = f"Cliclou no icone - {kwargs.get('search_term')}"

    if user_ip := request.META.get('HTTP_X_FORWARDED_FOR'):
        ip_address = user_ip.split(',')[0]
    else:
        ip_address = request.META.get('REMOTE_ADDR')
    user_agent = request.META.get('HTTP_USER_AGENT')
    is_mobile = 'Mobile' in user_agent
    try:
        with transaction.atomic():
            Services.objects.create(
                service=service,
                ip_address=ip_address,
                is_mobile=is_mobile
            )
    except Exception as e:
        print(e)

    return HttpResponse(status=200)
