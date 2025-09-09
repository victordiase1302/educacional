import openai
from django.conf import settings


def monitor_finetune_job(job_id):
    openai.api_key = settings.OPENAI
    finetuning_status = openai.Finetune.retrieve(id=job_id)
    return finetuning_status
