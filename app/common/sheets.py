"""
	This module implements google sheets handle data
"""

import gspread
from oauth2client.service_account import ServiceAccountCredentials
from app import app

# Google Sheet credentials
SCOPES = [
    'https://www.googleapis.com/auth/spreadsheets',
    'https://www.googleapis.com/auth/drive'
]
CREDS = ServiceAccountCredentials.from_json_keyfile_name(
    app.config['GOOGLE_SHEETS'], SCOPES
)
client = gspread.authorize(CREDS)

def get_data(spreadsheet_id: str) -> list:
	"""
	Get data from a spreadsheet

	Args:
		spreadsheet_id: The id of the spreadsheet to get data

	Returns:
		A list of data
	"""
	sheet = client.open_by_key(spreadsheet_id).sheet1
	return sheet.get_all_values()


def insert_data(spreadsheet_id: str, row: list) -> bool:
	"""
 	Registers an appointment with the veterinarian
  """
	try:
		sheet = client.open_by_key(spreadsheet_id).sheet1
		# Set row values to insert
		sheet.append_row(row)
		return True # Register successfully
	except:
		return False # Error register