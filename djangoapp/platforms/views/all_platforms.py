# from counters.views import service_counter
from core.decorators import block_direct_access
from django.conf import settings
from django.shortcuts import render
from platforms.models import Platform, StatusPlatform
from blog.models import Posts


@block_direct_access
def all_platforms(request):
    host = request.META.get('HTTP_HOST', '')
    qs = Platform.objects.filter(is_active=True)
    count = qs.count()
    # icons_set = set()
    # for obj in qs:
    #     icons_set.update(obj.icons.filter(
    #         is_filter=True, is_active=True)
    #     )
    icons_set = StatusPlatform.objects.filter(is_active=True, is_filter=True)
    id_posts_distinct = Posts.objects.values_list('site_setup_id', flat=True).distinct()
    icons_list = list(icons_set)
    ctx = {
        'page_title': 'Plataformas Analisadas',
        'count_platforms': count,
        "icons_list": icons_list,
        'id_posts_distinct': id_posts_distinct
    }
    if host in settings.SUB_DEV:
        return render(request, 'development/platforms.html', ctx)
    else:
        return render(request, "core/platforms.html", ctx)


def search_platform(request, *args, **kwargs):
    q = request.GET.get('q').strip()
    host = request.META.get('HTTP_HOST', '')
    qs = Platform.objects.filter(is_active=True)
    count_platforms = qs.count()

    if q == '':
        return _extracted_from_search_platform_8(
            qs, count_platforms, request, host
        )
    if q:
        qs = qs.filter(name__icontains=q)
        count_platforms = qs.count()
    # if search_term:
    #     qs = qs.filter(icons__name=search_term)
    if not qs:
        return render(
            request,
            'core/partials/search_not_found.html',
        )

    # icons_set = set()
    # for obj in qs:
    #     icons_set.update(obj.icons.filter(is_filter=True))
    # icons_list = list(icons_set)

    ctx = {
        'page_title': 'Plataformas Analisadas',
        "obj_list": qs,
        "count": count_platforms,
        # "icons_list": icons_list,
        "q": q
    }
    if host in settings.SUB_DEV:
        return render(
            request,
            'development/partials/list_search_platforms.html',
            ctx
        )
    else:
        return render(
            request,
            'core/partials/list_search_platforms.html',
            ctx
        )


# TODO Rename this here and in `search_platform`
def _extracted_from_search_platform_8(qs, count_platforms, request, host):
    # icons_set = set()
    # for obj in qs:
    #     icons_set.update(obj.icons.filter(is_filter=True, is_active=True))
    icons_set = StatusPlatform.objects.filter(is_active=True, is_filter=True)
    id_posts_distinct = Posts.objects.values_list('site_setup_id', flat=True).distinct()
    icons_list = list(icons_set)
    ctx = {
        'page_title': 'Plataformas Analisadas',
        'count_platforms': count_platforms,
        "icons_list": icons_list,
        "id_posts_distinct": id_posts_distinct
    }
    if host in settings.SUB_DEV:
        response = render(
            request, 'development/components/search_q_page.html', ctx
        )
    else:
        response = render(
            request, 'core/components/search_q_page.html', ctx
        )
    response["HX-Retarget"] = ".page-content"
    return response
