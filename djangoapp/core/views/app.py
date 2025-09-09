from core.decorators import block_direct_access
from django.shortcuts import render
from faq.models import FAQ
from platforms.models import Platform
from blog.models import Posts
from django.conf import settings
from django.db.models import Q


@block_direct_access
def app(request, *args, **kwargs):
    host = request.META.get('HTTP_HOST', '')
    print('host', host, sep='\n')
    qs = Platform.objects.filter(is_active=True)
    favorites = qs.filter(is_favorite=True)
    favs = qs.filter(is_payer=True)
    olds = qs.filter(is_old=True)

    if host in settings.SUB_DEV:
        lokup = Q(site_setup__title="Desenvolvimento")
        favorites = favorites.filter(lokup)
        favs = favs.filter(lokup)
        olds = olds.filter(lokup)
        qs = qs.filter(lokup)
    else:
        lokup = Q(site_setup__title="Desenvolvimento")
        favorites = favorites.exclude(lokup)
        favs = favs.exclude(lokup)
        olds = olds.exclude(lokup)
        qs = qs.exclude(lokup)
    favs = favs.order_by('-updated_at')[:2]
    favorites = favorites.order_by('-updated_at')
    olds = olds.order_by('-updated_at')
    qs = qs.order_by('-created_at')[:10]
    remaining_slots = (4 - favorites.count() % 4) % 4
    remaining_olds = (4 - olds.count() % 4) % 4
    remaining_favs = (2 - favs.count() % 2) % 2
    faqs = FAQ.objects.filter(is_active=True, in_main_page=True)
    id_posts_distinct = Posts.objects.values_list('site_setup_id', flat=True).distinct()
    ctx = {
        'obj_list': qs,
        'remaining_slots': remaining_slots,
        'favorites': favorites,
        'favs': favs,
        'olds': olds,
        'remaining_olds': remaining_olds,
        'remaining_favs': remaining_favs,
        'faqs': faqs,
        'id_posts_distinct':id_posts_distinct
    }
    if host in settings.SUB_DEV:
        return render(request, "development/index.html", ctx)
    else:
        return render(request, "core/index.html", ctx)
