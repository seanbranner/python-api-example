import os
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google.oauth2 import service_account
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
import sys
from pathlib import Path
from dotenv import load_dotenv
import os

load_dotenv()

try:
    project_path = Path(sys._MEIPASS)
except Exception:
    package_path = Path(os.path.abspath(__file__)).parent
    project_path = package_path.parent

class HandlgeGoogle:

    def __init__(self):
        self.scopes = ["https://www.googleapis.com/auth/spreadsheets"]
        self.spreadsheet_id = "1R9xnDA1zSQ1WTpX48oh9hnb-7a41c_C5hNf-YZgmsbY"
        self.credentials_file = str(project_path.joinpath("service_credentials.json"))
        self.token_path = "token.json"
        self.worksheet_name = 'Sheet1'
        self.cell_range = 'A:C'

        credential_info = eval(os.getenv('CREDENTIALS'))

        self.credentials = service_account.Credentials.from_service_account_info(info=credential_info)


        self.service_sheets = build('sheets', 'v4', credentials=self.credentials)
        self.sheets = self.service_sheets.spreadsheets()

    def update_google_sheet(self,values,spreadsheet_id,worksheet_name,cell_range):

        value_range_body = {
            'majorDimension': 'ROWS',
            'values': values
        }
        self.sheets.values().update(
            spreadsheetId=spreadsheet_id,
            valueInputOption="USER_ENTERED",
            range=worksheet_name + '!' + cell_range,
            body=value_range_body
        ).execute()

    def read_google_sheet(self):

        results = self.sheets.values().get(
            spreadsheetId=self.spreadsheet_id,
            range=f"{self.worksheet_name}!{self.cell_range}"
        ).execute()

        values = results.get('values', [])

        return values