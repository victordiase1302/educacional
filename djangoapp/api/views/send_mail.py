import threading

from django.conf import settings
from django.core.mail import send_mail
from django.template.loader import render_to_string


class SendEmailForEbook(threading.Thread):
    def __init__(self, *args, **kwargs):
        threading.Thread.__init__(self)
        self.email_sending = kwargs.get("email")
        self.name = kwargs.get("name", None)
        self.uuid = kwargs.get("uuid")

    def run(self):
        url = f"https://econometriafacil.com.br/baixar-ebook/"
        template = "mailers/register.txt"
        subject = "[EconometriaFacil] - Seu ebook está aqui"
        message = render_to_string(
            template,
            {
                "name": self.name,
                "url": url,
            },
        )
        try:
            send_mail(
                subject,
                message,
                "contato@econometriafacil.com.br",
                [
                    self.email_sending,
                ],
                html_message=message,
                fail_silently=False,
            )

        except Exception as e:
            print("Error Email:", e)
