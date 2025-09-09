from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
from notifications.consumers import NotificationConsumer
from django.urls import path

application = ProtocolTypeRouter({    
    'websocket': AuthMiddlewareStack(
        URLRouter([
            path("ws/notifications/", NotificationConsumer.as_asgi()),
        ])
    ),
})
