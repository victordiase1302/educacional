from chat.consumers import OpenaiConsumer
from django.urls import path, re_path

from . import consumers

websocket_urlpatterns = [
    path("ws/notifications/", consumers.NotificationConsumer.as_asgi()),
    path("ws/chat/", OpenaiConsumer.as_asgi()),
]
