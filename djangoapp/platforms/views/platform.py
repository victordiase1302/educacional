# from core.decorators import block_direct_access
import threading

from counters.views import increment_counter
from django.shortcuts import render
from platforms.models import Platform


# @block_direct_access
def platform(request, *args, **kwargs):
    referer = request.META.get("HTTP_REFERER")
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
    pltf = Platform.objects.filter(slug=slug).first()
    formatted_text = pltf.description.replace(
        ';', '</p><p class="para-title">'
    )
     
    ctx = {
        'page_title': 'Detalhes da Plataforma',
        'obj': pltf,
        'description': formatted_text,
        'is_count': is_count,
        'referer': referer,    
    }
    return render(
        request,
        'core/platform-detail.html',
        ctx
    )
