import time

from api.views.send_mail import SendEmailForEbook
from celery import shared_task
from celery.utils.log import get_task_logger
from ecr.utils import (
    filter_new_leads,
    filtering_new_records,
    get_entries_from_spreadsheet,
    register_new_leads,
)

logger = get_task_logger(__name__)


@shared_task(name="task_job_read_spreadsheet")
def task_read_spreadsheet():
    logger.info("Iniciando execução do job lendo a planilha")
    observe_the_spreadsheet()
    logger.info("Encerrando execução do job lendo a planilha")


def observe_the_spreadsheet():
    results = get_entries_from_spreadsheet()

    new_results = filtering_new_records(results)

    new_leads = filter_new_leads(new_results)
    register_new_leads(new_leads)
    for lead in new_leads:
        SendEmailForEbook(
            name=lead["nome"],
            uuid="xxx",
            email=lead["email"],
        ).start()
        time.sleep(0.25)

    return
