from core.models import ArquivoS3, EbookDownload
from django.contrib import admin

# Register your models here.


@admin.register(EbookDownload)
class EbookDownloadAdmin(admin.ModelAdmin):
    list_display = ("title", "ip_address", "user_agent", "timestamp")
    search_fields = ("title", "ip_address", "user_agent")
    list_filter = ("timestamp",)
    date_hierarchy = "timestamp"
    readonly_fields = ("timestamp",)


@admin.register(ArquivoS3)
class ArquivoS3Admin(admin.ModelAdmin):
    list_display = (
        "titulo",
        "slug",
        "data_upload",
        "tipo_arquivo",
        "is_active",
    )
    search_fields = ("titulo", "slug")
    list_filter = ("data_upload", "tipo_arquivo")
    readonly_fields = ("created_at", "updated_at")
