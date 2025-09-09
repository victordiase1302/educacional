from chat import views
from django.urls import path

app_name = 'chat'

urlpatterns = [
    path('', views.index, name='index'),
    path('export/', views.export, name='export'),
]
