from __future__ import absolute_import, unicode_literals

from datetime import datetime, timedelta

from celery import shared_task
from celery.utils.log import get_task_logger
from notifications.models import Notification
from notifications.views import send_notifications

logger = get_task_logger(__name__)


@shared_task(name='task_job_schedule_notification')
def schedule_notification():
    logger.info("Iniciando execução do job agenda as tarefas")
    print('Agendado')
    logger.info("Encerrando execução do job agenda as tarefas")


@shared_task
def check_for_notifications():
    now = datetime.now()
    notifications = Notification.objects.filter(
        date_to_send=now.date(),
        time_to_send__gte=(now - timedelta(minutes=1)).time(),
        time_to_send__lte=now.time()
    )

    for notification in notifications:
        send_notifications(notification)
        if notification.days_to_repeat > 0:
            notification.date_to_send += timedelta(days=1)
            notification.days_to_repeat -= 1
            notification.save()
