import csv
from datetime import datetime

from django import forms
from django.contrib import messages
from django.shortcuts import redirect, render
from django.utils import timezone
from platforms.models import Platform


class UploadCsvForm(forms.Form):
    csv_file = forms.FileField()


def upload_csv(modeladmin, request, queryset):
    form = UploadCsvForm()
    payload = {
        'form': form,
    }

    return render(
        request,
        'admin/upload_csv.html',
        payload
    )

upload_csv.short_description = "Upload CSV"


def upload_other_csv(request):
    if 'apply' in request.POST:
        csv_file = request.FILES['csv_file']
        # Verificar se não é um arquivo CSV
        if not csv_file.name.endswith('.csv'):
            messages.error(request, 'Isso não é um arquivo CSV.')
            return redirect("..")

        file_data = csv_file.read().decode('utf-8')
        lines = file_data.split("\n")

        # Loop sobre as linhas e salve-as no banco de dados. Pule o cabeçalho
        for line in lines[1:]:
            fields = line.split(",")
            if len(fields) == 2:
                id_str, created_at_str = fields
                try:
                    obj = Platform.objects.get(id=id_str.strip())
                    dt_obj = datetime.strptime(created_at_str.strip(), '%d/%m/%Y %H:%M')
                    dt_obj = timezone.make_aware(dt_obj)
                    obj.created_at = dt_obj
                    obj.save()
                except Exception as e:
                    messages.error(request, f"Erro ao atualizar o objeto com ID {id_str}: {e}")
                print(obj)
        messages.success(request, "Seu arquivo CSV foi importado com sucesso.")
        return redirect("..")

    form = UploadCsvForm()
    payload = {
        'form': form,
    }

    return render(
        request,
        'admin/upload_csv.html',
        payload
    )
