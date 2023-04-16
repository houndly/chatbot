"""
	This module implements google sheets handle data
"""
import os.path
from typing import List, Dict
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from app.common.constants import CredentialsFiles
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from oauth2client.service_account import ServiceAccountCredentials
from app import app

# Google Sheet credentials
SCOPES = ['https://www.googleapis.com/auth/spreadsheets']
CREDS = ServiceAccountCredentials.from_json_keyfile_name(
    app.config['GOOGLE_SHEETS_CREDS_FILE'], SCOPES)

def get_credentials() -> Credentials:
    """
    Get the user's credentials from a file or prompt the user to log in.
    """
    creds = None
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(CredentialsFiles.GOOGLE_SHEETS, SCOPES)
            creds = flow.run_local_server(port=0)
        with open('token.json', 'w') as token:
            token.write(creds.to_json())
    return creds

def getConnection(spreadsheet_id: str) -> build:
    """Get a connection to a Google Sheets spreadsheet"""
    credentials = get_credentials()
    try:
        service = build('sheets', 'v4', credentials=credentials)
        sheet_metadata = {'properties': {'title': 'My Spreadsheet'}}
        spreadsheet = service.spreadsheets().create(body=sheet_metadata,fields='spreadsheetId').execute()
        spreadsheet_id = spreadsheet.get('spreadsheetId')
        sheet = service.spreadsheets().get(spreadsheetId=spreadsheet_id,includeGridData=True).execute()
        sheet_id = sheet['sheets'][0]['properties']['sheetId']
        return service.spreadsheets()
    except HttpError as err:
        print(err)
        return None

def register_appointment(spreadsheet_id: str, date: str, time: str, pet_name: str, species: str, breed: str, age: int, sex: str, owner_name: str, owner_phone: str, reason: str, notes: str) -> None:
    """Registers an appointment with the veterinarian"""
    sheet = getConnection(spreadsheet_id)
    new_row = [pet_name, species, breed, age, sex, owner_name, owner_phone, date, time, reason, notes]
    sheet.values().append(spreadsheetId=spreadsheet_id, range='Citas!A2', valueInputOption='USER_ENTERED', body={'values': [new_row]}).execute()

# TODO: Delete after generate correct usage
# def main() -> None:
#     spreadsheet_id = '1LzQJpEUbIvpc2NEJQM8pWvbPv4X6QqCwJ5Z54KSUMiI'
#     date = '2023-04-10'
#     time = '10:00 AM'
#     pet_name = 'Max'
#     species = 'Dog'
#     breed = 'Labrador Retriever'
#     age = 3
#     sex = 'Male'
#     owner_name = 'John Doe'
#     owner_phone = '555-1234'
#     reason = 'Annual checkup'
#     notes = 'Max is generally healthy, but has been experiencing some minor digestive issues.'

#     # Register the appointment
#     register_appointment(spreadsheet_id, date, time, pet_name, species, breed, age, sex, owner_name, owner_phone, reason, notes)

#     print('Appointment registered successfully!')
