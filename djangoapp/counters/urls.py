from counters import views
from django.urls import path

app_name = 'counters'


urlpatterns = [
    path('', views.service_counter, name='service'),
]
