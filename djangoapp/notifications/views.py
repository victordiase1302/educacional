import json
from datetime import datetime, timedelta

from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer
from django.db.models import Q
from django.shortcuts import render
from notifications.models import Notification


def send_unread_notifications(request):
    ids_lidas_str = request.GET.get('ids_lidas')
    site_setup = request.GET.get('site_setup')
    ids_lidas = []
    if ids_lidas_str != 'null':
        try:
            ids_lidas = json.loads(ids_lidas_str)
            ids_lidas = [int(id) for id in ids_lidas]
        except (json.JSONDecodeError, ValueError):
            ids_lidas = []
    now = datetime.now()
    one_day_later = now - timedelta(hours=24)
    qs = Notification.objects.select_related('site_setup')
    qs = qs.filter(is_active=True)
    qs = qs.filter(created_at__gte=one_day_later)
    qs = qs.filter(site_setup=site_setup)
    # qs = qs.filter(~Q(id__in=ids_lidas))
    qs = qs.filter(time_to_send__lte=(now - timedelta(minutes=1)).time())
    qs = qs.filter(time_to_send__gte=now.time())
    unread_ids = list(qs.values_list('id', flat=True))
    ctx = {'obj_list': qs, 'unread_ids': unread_ids}
    return render(
        request, "development/components/list_unread_notifications.html", ctx
    )


def send_notifications(instance):
    if instance.is_active:
        channel_layer = get_channel_layer()
        group_name = 'user-notifications'
        event = {
            'type': 'user_mensage',
            'text': instance.message,
            'color': instance.color,
            'emoji': instance.emoji,
            'link': instance.link,
            'id_notification': instance.id,
            'site_active': instance.site_setup.id,
        }
        async_to_sync(channel_layer.group_send)(group_name, event)
