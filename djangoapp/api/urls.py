from django.urls import path

from .views import SendEmailEbook, UserStatistics

urlpatterns = [
    # path('user-stats/', UserStatistics.as_view(), name='user-stats'),
    path(
        "enviar-email/<str:email>/",
        SendEmailEbook.as_view(),
        name="send_email",
    ),
]
