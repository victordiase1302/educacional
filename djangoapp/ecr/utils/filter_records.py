from datetime import datetime, timedelta

from django.utils.timezone import make_aware
from ecr.models import Lead


def filtering_new_records(results):
    now = make_aware(datetime.now())
    five_minutes_late = now - timedelta(minutes=5)
    new_results = []
    for result in results:
        data_hora_str = result[0]
        nome = result[1]
        email = result[2]

        data_hora = datetime.strptime(data_hora_str, "%d/%m/%Y %H:%M:%S")
        data_hora = make_aware(data_hora)

        if five_minutes_late <= data_hora <= now:
            new_results.append(
                {
                    "data_hora": data_hora,
                    "nome": nome,
                    "email": email,
                }
            )

    return new_results


def filter_new_leads(novos_registros):
    """Filtra apenas os leads que ainda não estão cadastrados"""
    emails_existentes = Lead.objects.filter(
        email__in=[r["email"] for r in novos_registros]
    ).values_list("email", flat=True)

    novos_leads = [r for r in novos_registros if r["email"] not in emails_existentes]

    return novos_leads


def register_new_leads(novos_leads):
    """Cadastra novos leads no banco de dados"""
    new_leads_objs = [
        Lead(first_name=lead["nome"], email=lead["email"], message="", is_active=True)
        for lead in novos_leads
    ]

    Lead.objects.bulk_create(new_leads_objs)

    return new_leads_objs
