import os

import google.auth
from api.views.send_mail import SendEmailForEbook
from django.conf import settings
from ecr.tasks.read_spreadsheet import observe_the_spreadsheet
from google.oauth2.service_account import Credentials
from googleapiclient.discovery import build
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView


class SendEmailEbook(APIView):
    def post(self, request, *args, **kwargs):
        email = kwargs.get("email")
        print(request)
        print(email, "email")
        data = {"success": True}
        return Response(data, status=status.HTTP_200_OK)

    def get(self, request, *args, **kwargs):
        observe_the_spreadsheet()
        values = ""
        # print(values[-1], "!!" * 10)
        # email = values[-1]
        # SendEmailForEbook(
        #     name=email[0],
        #     uuid="xxx",
        #     email=email[1],
        # ).start()
        # email = kwargs.get("email")
        # print(email, "email")
        data = {"success": True}
        return Response(data, status=status.HTTP_200_OK)
