from django.conf import settings
from django.http import HttpResponseRedirect


def block_direct_access(view_func):
    def _wrapped_view_func(request, *args, **kwargs):
        allowed_start_urls = settings.ALLOWED_START

        referer = request.META.get("HTTP_REFERER", "")
        if not any(referer.startswith(url) for url in allowed_start_urls):
            return HttpResponseRedirect("/")
        return view_func(request, *args, **kwargs)

    return _wrapped_view_func
