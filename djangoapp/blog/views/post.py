from django.shortcuts import render
from blog.models import Posts
from django.conf import settings


def post(request, *args, **kwargs):
    referer = request.META.get("HTTP_REFERER")
    host = request.META.get('HTTP_HOST', '')
    is_count = False
    if request.GET.get('ref') or not referer:
        is_count = True
        referer = (
            request.GET.get('ref') or request.META.get('HTTP_REFERER') 
        ) or 'HTTP'
        # thread = threading.Thread(target=increment_counter, args=(request,))
        # thread.start()
    # print(is_count, '<<<<<')
    slug = kwargs.get('slug')
    post = Posts.objects.filter(slug=slug).first()
    # formatted_text = pltf.description.replace(
    #     ';', '</p><p class="para-title">'
    # )    
    ctx = {
        'page_title': post.title,
        'obj': post,
        'is_count': is_count,
        'referer': referer,
        # 'description': formatted_text,
    }
    if host in settings.SUB_DEV:
        return render(
            request,
            'development/partials/post_detail.html',
            ctx
        )
    return render(
        request,
        'core/partials/post_detail.html',
        ctx
    )
