"""
	This module implements google sheets handle data
"""
import os.path
from typing import List
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from app.common.constants import CredentialsFiles
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

# Google Sheet credentials
SCOPES = ['https://www.googleapis.com/auth/spreadsheets']
SPREADSHEET_ID = '1FUrbjPW4pcSNh43zp2dIK3YyQNgQ7BQZ613CU7ugz2E' # TODO: ADD into .env file
RANGE_NAME = 'Class Data!A2:E'

def get_credentials() -> Credentials:
	"""
	Get the user's credentials from a file or prompt the user to log in.
	"""
	creds = None
	# Create a temporary token file to handle insertion of data
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

def getConnection() -> build:
	"""
	Get a connection to a Google Sheets spreadsheet
	"""
	credentials = get_credentials()
	try:
		service = build('sheets', 'v4', credentials = credentials)
		# sheet_metadata = {'properties': {'title': 'My Spreadsheet'}}
		# spreadsheet = service.spreadsheets().create(fields = 'spreadsheetId').execute()
		# spreadsheet_id = spreadsheet.get('spreadsheetId')
		# sheet = service.spreadsheets().get(spreadsheetId = spreadsheet_id, includeGridData = True).execute()
		# sheet_id = sheet['sheets'][0]['properties']['sheetId']
		return service.spreadsheets()
	except HttpError as err:
		print(err)
		return None

def get_data(range_name: str) -> List[List[str]]:
	"""
	Get data from a Google Sheets spreadsheet
	"""
	try:
		service = getConnection()
		result = service.values().get(spreadsheetId=SPREADSHEET_ID, range=range_name).execute()
		return result.get('values', [])
	except HttpError as err:
		print(err)
		return None

def insert_data(row: List) -> bool:
	"""
 	Registers an appointment with the veterinarian
  """
	try:
		sheet = getConnection()
		# Set row values to insert
		sheet.values().append(range='Citas!A2', valueInputOption = 'USER_ENTERED', body = {'values': [row]}).execute()
		return True # Register successfully
	except:
		return False # Error register