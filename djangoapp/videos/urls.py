from django.urls import path
from videos.views import play_video

app_name = "videos"

urlpatterns = [
    path('play/', play_video, name='play')
]
