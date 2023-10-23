import os
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google.oauth2 import service_account
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError



def update_google_sheet(values,spreadsheet_id,worksheet_name,cell_range):

    value_range_body = {
        'majorDimension': 'ROWS',
        'values': values
    }
    sheets.values().update(
        spreadsheetId=spreadsheet_id,
        valueInputOption="USER_ENTERED",
        range=worksheet_name + '!' + cell_range,
        body=value_range_body
    ).execute()

def read_google_sheet(sheets,spreadsheet_id,worksheet_name,cell_range):

    results = sheets.values().get(
        spreadsheetId=spreadsheet_id,
        range=worksheet_name+'!'+cell_range
    ).execute()

    values = results.get('values', [])

    for row in values:
        print(row)

if __name__ == '__main__':
    scopes = ["https://www.googleapis.com/auth/spreadsheets"]
    spreadsheet_id = "1R9xnDA1zSQ1WTpX48oh9hnb-7a41c_C5hNf-YZgmsbY"
    credentials_file = "service_credentials.json"
    token_path = "token.json"
    worksheet_name = 'Sheet1'
    cell_range = 'A8:C8'

    credentials = service_account.Credentials.from_service_account_file(filename=credentials_file)

    service_sheets = build('sheets', 'v4', credentials=credentials)
    sheets = service_sheets.spreadsheets()

    input_values = (
        ('8', '80', 'h'),
    )

    update_google_sheet(input_values,spreadsheet_id,worksheet_name,cell_range)

    read_google_sheet(sheets,spreadsheet_id,worksheet_name,cell_range)
