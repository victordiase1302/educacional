import csv

from django.contrib import admin
from django.http import HttpResponse


@admin.action(description="Exportar Selecionados para CSV")
def export_as_csv(self, request, queryset):
    meta = self.model._meta
    field_names = ['Nº do Visitante', 'IP', 'De onde', 'D. Movel', 'Data']
    response = HttpResponse(content_type="text/csv")
    response["Content-Disposition"] = f"attachment; filename={meta}.csv"
    writer = csv.writer(response)
    writer.writerow(field_names)
    output = [
        [
            obj.pk,
            obj.ip_address,
            obj.referer,
            obj.is_mobile,
            obj.get_format_as_timezone
        ]
        for obj in queryset
    ]
    writer.writerows(output)
    return response


@admin.action(description="Exportar Selecionados para CSV")
def export_service_as_csv(self, request, queryset):
    meta = self.model._meta
    field_names = ['Serviço', 'IP', 'D. Movel', 'Data']
    response = HttpResponse(content_type="text/csv")
    response["Content-Disposition"] = f"attachment; filename={meta}.csv"
    writer = csv.writer(response)
    writer.writerow(field_names)
    output = [
        [
            obj.service,
            obj.ip_address,
            obj.is_mobile,
            obj.get_format_as_timezone
        ]
        for obj in queryset
    ]
    writer.writerows(output)
    return response
