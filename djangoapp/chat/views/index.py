from blog.models import Posts
from django.conf import settings
from django.shortcuts import render


def index(request, *args, **kwargs):
    host = request.META.get('HTTP_HOST', '')
    id_posts_distinct = Posts.objects.values_list('site_setup_id', flat=True).distinct()
    ctx = {
        'page_title': 'Chat Pinóia',
        'posts': 'posts',
        'id_posts_distinct': id_posts_distinct
    }
    if host in settings.SUB_DEV:
        return render(request, 'development/chat.html', ctx)
    return render(request, 'core/posts.html', ctx)
