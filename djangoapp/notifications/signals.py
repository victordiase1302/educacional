from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer
from django.db.models.signals import post_save
from django.dispatch import receiver
from notifications.models import Notification


@receiver(post_save, sender=Notification)
def send_notifications(sender, instance, created, **kwargs):
    if instance.is_active and not instance.date_to_send:
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
