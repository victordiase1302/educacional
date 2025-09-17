from django.urls import path
from iprof import views

app_name = "iprof"

urlpatterns = [
    path("", views.index_view, name="index"),
    path("obrigado/", views.obrigado_view, name="obrigado"),
]
