from counters.models import Services, Visit
from counters.utils.export_csv import export_as_csv, export_service_as_csv
from django.contrib import admin
from django.contrib.admin.models import LogEntry
from platforms.utils.search_for_date import BaseDateSearchModelAdmin

@admin.register(Visit)
class VisitAdmin(BaseDateSearchModelAdmin):
    list_display = "id", "ip_address", "referer", "is_mobile", "is_pwa", "is_iphone", "created_at"
    readonly_fields = ("created_at",)
    search_fields = 'created_at', 'is_mobile'
    ordering = [
        "-id",
    ]
    list_per_page = 25
    date_hierarchy = "created_at"
    list_filter = ["created_at"]
    actions = [export_as_csv]


# @admin.register(Services)
# class ServicesAdmin(BaseDateSearchModelAdmin):
#     list_display = "id", "service", "ip_address", "is_mobile", "created_at"
#     readonly_fields = ("created_at",)
#     search_fields = 'created_at', 'is_mobile'
#     ordering = [
#         "-id",
#     ]
#     list_per_page = 25
#     date_hierarchy = "created_at"
#     list_filter = ["created_at"]
#     actions = [export_service_as_csv]


# @admin.register(LogEntry)
# class LogEntryAdmin(admin.ModelAdmin):
#     # to have a date-based drilldown navigation in the admin page
#     date_hierarchy = 'action_time'

#     # to filter the resultes by users, content types and action flags
#     list_filter = [
#         'user',
#         'content_type',
#         'action_flag'
#     ]

#     # when searching the user will be able to search in both object_repr and change_message
#     search_fields = [
#         'object_repr',
#         'change_message'
#     ]

#     list_display = [
#         'action_time',
#         'user',
#         'content_type',
#         'action_flag',
#     ]
