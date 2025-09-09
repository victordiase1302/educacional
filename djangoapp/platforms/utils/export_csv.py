import csv

from django.contrib import admin
from django.http import HttpResponse


@admin.action(description="Exportar Selecionados para CSV")
def export_as_csv(self, request, queryset):
    meta = self.model._meta
    field_names = [
        'ID',
        'Nome da plataforma',
        'Nome da família',
        'Status',
        'Depósito mínimo',
        'Saque mínimo',
        'Bonus',
        'Link',
        'Data'
    ]
    response = HttpResponse(content_type="text/csv")
    response["Content-Disposition"] = f"attachment; filename={meta}.csv"
    writer = csv.writer(response)
    writer.writerow(field_names)
    output = [
        [
            obj.pk,
            obj.name,
            obj.family_name,
            obj.status,
            obj.min_deposit,
            obj.min_cash,
            obj.bonus,
            obj.lucky_link,
            obj.get_format_as_timezone,
        ]
        for obj in queryset
    ]
    writer.writerows(output)
    return response
