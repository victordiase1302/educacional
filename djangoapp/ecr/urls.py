from ecr import views
from django.urls import path

app_name = "ecr"

urlpatterns = [
    path("create/", views.create, name="create"),
    path(
        "politica-de-privacidade/",
        views.privacy_policy,
        name="privacy_policy",
    ),
    # path('count/', views.count, name='count'),
    # path('', views.index, name='index'),
]
