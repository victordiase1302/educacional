import os

from django.conf import settings
from google.oauth2.service_account import Credentials
from googleapiclient.discovery import build


def get_entries_from_spreadsheet():
    SCOPES = ["https://www.googleapis.com/auth/spreadsheets.readonly"]
    SPREADSHEET_ID = "13M5nbSiuxgno5UJhArr6ycFgBv7Z-yncZrYLgS6WWcU"
    RANGE_NAME = "Respostas ao forms 1º lançamento EF!A:C"
    path_credentials = os.path.join(
        settings.BASE_DIR,
        "energymap-392701-9f0a062955eb.json",
    )
    creds = Credentials.from_service_account_file(
        path_credentials,
        scopes=SCOPES,
    )
    service = build("sheets", "v4", credentials=creds)
    sheet = service.spreadsheets()
    result = (
        sheet.values()
        .get(
            spreadsheetId=SPREADSHEET_ID,
            range=RANGE_NAME,
        )
        .execute()
    )
    values = result.get("values", [])
    if not values:
        return None

    return values[1:]
