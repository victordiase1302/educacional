from core import views
from django.urls import path

app_name = "core"

urlpatterns = [
    # path('app/', views.app, name='app'),
    # path('count/', views.count, name='count'),
    path(
        "download/<slug:slug>/",
        views.download_by_slug,
        name="download_by_slug",
    ),
    path("", views.index, name="index"),
    path("sobre/", views.about, name="about"),
    path("baixar-ebook/", views.download_file, name="download_ebook"),
]
