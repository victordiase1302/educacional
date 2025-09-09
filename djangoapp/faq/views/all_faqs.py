from core.decorators import block_direct_access
from django.shortcuts import render
from faq.models import Section


@block_direct_access
def all_faqs(request, *args, **kwargs):
    sections = Section.objects.filter(is_active=True)
    ctx = {
        'page_title': 'Dúvidas Frequentes',
        'sections': sections
    }
    return render(request, "core/faqs.html", ctx)
