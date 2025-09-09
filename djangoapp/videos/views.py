from django.shortcuts import render


def play_video(request, *args, **kwargs):
    video_link = request.GET.get('video_link')
    video_title = request.GET.get('video_title')
    video_link = f'{video_link}?&autoplay=1'
    ctx = {
        'video_link': video_link,
        'video_title': video_title
    }
    return render(request, "development/components/iframe_video.html", ctx)
