import os

import django
from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
from chat.consumers import OpenaiConsumer
# from channels.security.websocket import AllowedHostsOriginValidator
from django.core.asgi import get_asgi_application
# from channels.routing import get_default_application
from django.urls import path
from notifications.consumers import NotificationConsumer

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "project.settings")

django.setup()

django_asgi_app = get_asgi_application()

import notifications.routing

application = ProtocolTypeRouter({
    "http": django_asgi_app,
    'websocket': AuthMiddlewareStack(
        URLRouter([
            path("ws/notifications/", NotificationConsumer.as_asgi()),
            path("ws/chat/", OpenaiConsumer.as_asgi()),
        ])
    ),
})
