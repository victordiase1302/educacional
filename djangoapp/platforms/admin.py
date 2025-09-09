# from django.contrib import admin
# from platforms import models
# from platforms.utils.export_csv import export_as_csv

# from platforms.utils.search_for_date import BaseDateSearchModelAdmin
# # @admin.register(models.Icon)
# # class IconAdmin(admin.ModelAdmin):
# #     list_display = 'id', 'title', 'order', 'is_active'
# #     list_display_links = 'id', 'title'
# #     search_fields = 'id', 'title'
# #     # inlines = CardTargetPlatformInline,
# #     readonly_fields = 'created_at', 'updated_at'


# class StatusIsNullFilter(admin.SimpleListFilter):
#     title = 'Status Nulos'
#     parameter_name = 'status__isnull'

#     def lookups(self, request, model_admin):
#         return [
#             ('True', 'Sem Status'),
#             ('False', 'Com Status'),
#         ]

#     def queryset(self, request, queryset):
#         value = self.value()
#         if value == 'True':
#             return queryset.filter(status__isnull=True)
#         elif value == 'False':
#             return queryset.filter(status__isnull=False)


# class StatusNameFilter(admin.SimpleListFilter):
#     title = 'Nome dos Status'
#     parameter_name = 'status__name'

#     def lookups(self, request, model_admin):
#         qs = models.StatusPlatform.objects.filter(is_filter=True)
#         names = qs.values_list('name', flat=True).distinct()
#         return [(name, name) for name in names]

#     def queryset(self, request, queryset):
#         if value := self.value():
#             return queryset.filter(status__name=value)


# class IconsNameFilter(admin.SimpleListFilter):
#     title = 'Nome dos Icones'
#     parameter_name = 'icons__name'

#     def lookups(self, request, model_admin):
#         names = models.StatusPlatform.objects.values_list(
#             'name', flat=True
#         ).distinct()
#         lookup_options = [(name, name) for name in names]
#         lookup_options.append(('None', 'Nenhum'))
#         return lookup_options

#     def queryset(self, request, queryset):
#         if self.value() == 'None':
#             return queryset.filter(icons__name__isnull=True)
#         if value := self.value():
#             return queryset.filter(icons__name=value)


# @admin.register(models.SpecificDetail)
# class SpecificDetailAdmin(admin.ModelAdmin):
#     list_display = 'id', 'title', 'order', 'is_active'
#     list_display_links = 'id', 'title'
#     search_fields = 'id', 'title'
#     # inlines = CardTargetPlatformInline,
#     readonly_fields = 'created_at', 'updated_at'


# @admin.register(models.StatusPlatform)
# class StatusPlatformAdmin(admin.ModelAdmin):
#     list_display = 'id', 'name', 'cor_hex', 'order', 'is_filter', 'is_active'
#     list_display_links = 'id', 'name'
#     search_fields = 'id', 'name'
#     list_editable = 'cor_hex', 'order', 'is_filter', "is_active"
#     # inlines = CardTargetPlatformInline,
#     readonly_fields = 'created_at', 'updated_at'


# @admin.register(models.Platform)
# class PlatformAdmin(BaseDateSearchModelAdmin):
#     list_display = (
#         'id',
#         'name',
#         'family_name',
#         'order',
#         'is_payer',
#         'is_favorite',
#         'is_old',
#         'is_active'
#     )
#     list_display_links = 'id', 'name'
#     search_fields = 'id', 'name', 'family_name', 'status__name'
#     list_editable = 'order', "is_payer", "is_favorite", 'is_old', "is_active",
#     filter_horizontal = ("icons", "specific_detail")
#     list_filter = [
#         StatusNameFilter, IconsNameFilter, 'is_active', StatusIsNullFilter, "is_payer"
#     ]
#     ordering = ['-pk', '-updated_at']
#     # inlines = CardTargetPlatformInline,
#     readonly_fields = 'created_at', 'updated_at'
#     actions = [export_as_csv]
