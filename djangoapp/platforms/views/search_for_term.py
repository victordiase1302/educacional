from django.conf import settings
from django.shortcuts import render
from platforms.models import Platform, StatusPlatform


def search_for_term(request, *args, **kwargs):
    search_term = request.GET.get('search_term', '').strip()
    host = request.META.get('HTTP_HOST', '')
    all_plt = Platform.objects.filter(is_active=True)
    if search_term:
        qs = all_plt.filter(icons__name=search_term)
        qs = qs.order_by('-created_at')
    # icons_set = set()
    # for obj in all_plt:
    #     icons_set.update(obj.icons.filter(is_filter=True).order_by('-order'))
    icons_set = StatusPlatform.objects.filter(is_active=True, is_filter=True)
    count_platforms = qs.count()
    icons_list = list(icons_set)

    ctx = {
        'page_title': 'Plataformas Analisadas',
        "obj_list": qs,
        "count": count_platforms,
        "icons_list": icons_list,
        "search_term": search_term
    }
    if host in settings.SUB_DEV:
        return render(
            request,
            'development/partials/list_search_for_badge.html',
            ctx
        )
    else:
        return render(
            request,
            'core/partials/list_search_for_badge.html',
            ctx
        )
