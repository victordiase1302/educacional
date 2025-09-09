from django.contrib import admin
from ecr.models.leeds import Lead

@admin.register(Lead)
class LeadAdmin(admin.ModelAdmin):
    list_display = ("email", "created_at", "is_active")
    search_fields = ("email",)
    list_filter = ("is_active",)
    date_hierarchy = "created_at"
    readonly_fields = ("created_at", "updated_at")
    fieldsets = (
        (
            "Dados do Lead",
            {
                "fields": (
                    "email",
                    "message",
                    "is_active",
                )
            },
        ),
        (
            "Informações de controle",
            {
                "fields": (
                    "created_at",
                    "updated_at",
                )
            },
        ),
    )
    actions = ["activate", "deactivate"]

    def activate(self, request, queryset):
        queryset.update(is_active=True)

    activate.short_description = "Ativar leeds"

    def deactivate(self, request, queryset):
        queryset.update(is_active=False)

    deactivate.short_description = "Desativar leeds"
