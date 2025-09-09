from django.urls import path
from notifications.views import send_unread_notifications
app_name = "notifications"

urlpatterns = [
    path('nao-lidas/', send_unread_notifications, name='unread_notifications'),
]
