from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path(settings.DJANGO_ADMIN_URL, admin.site.urls),
    # path('users/', include('users.urls')),
    # path('plataformas/', include('platforms.urls')),
    # path('counters/', include('counters.urls')),
    # path('videos/', include('videos.urls')),
    # path('faqs/', include('faq.urls')),
    # path('blog/', include('blog.urls')),
    # path('chat/', include('chat.urls')),
    # path('notificacoes/', include('notifications.urls')),
    path("", include("pwa.urls")),
    path("", include("core.urls")),
    path("", include("development.urls")),
    path("ecr/", include("ecr.urls")),
    path("iprof/", include("iprof.urls")),
    path("api/v1/", include("api.urls")),
]

if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT,
    )


admin.site.site_header = "Daniel Fortune"
admin.site.site_title = "Daniel Fortune Painel ADM"
admin.site.index_title = "Bem-vindo ao Daniel Fortune"
