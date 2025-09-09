# from django import forms
# from django.contrib import admin
# from notifications.models import Notification


# @admin.register(Notification)
# class NotificationAdmin(admin.ModelAdmin):
#     # class Media:
#     #     css = {
#     #         'all': (f'{settings.STATIC_URL}/development/css/style_adm.css',)
#     #     }
#     def formfield_for_dbfield(self, db_field, **kwargs):
#         if db_field.name == 'message':
#             kwargs['widget'] = forms.Textarea(attrs={'rows': 4, 'cols': 80})
#         return super(NotificationAdmin, self).formfield_for_dbfield(
#             db_field, **kwargs
#         )

#     def has_change_permission(self, request, obj=None):
#         if obj:
#             return False
#         return super().has_change_permission(request, obj)

#     list_display = (
#         'id',
#         'site_setup',
#         'message',
#         'date_to_send',
#         'time_to_send',
#         'days_to_repeat',
#         'is_active'
#     )
#     list_display_links = 'id', 'site_setup', 'message'
#     search_fields = 'id', 'message'
#     list_editable = "is_active",
#     # inlines = CardTargetPlatformInline,
#     readonly_fields = 'created_at', 'updated_at',
