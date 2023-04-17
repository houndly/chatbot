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

def get_appointments(spreadsheet_id: str) -> list:
    """
        Get all appointments from the given spreadsheet.

        Args:
            spreadsheet_id: The id of the spreadsheet to get the appointments from.

        Returns:
            A list of dictionaries containing the appointments.
    """
    sheet = client.open_by_key(spreadsheet_id).sheet1
    data = sheet.get_all_values()
    data = data[3:]  # Remove the header and the first empty row

    appointments = []
    for row in data:
        appointments.append({
            "Mascota": row[2],
            "Fecha": row[5],
            "Hora": row[6],
        })

    return appointments




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