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


def get_sheet_data(spreadsheet_id: str, worksheet: str) -> list:
    """
    Get data from a spreadsheet

    Args:
            spreadsheet_id: The id of the spreadsheet to get data

    Returns:
            A list of data
    """
    sheet = client.open_by_key(spreadsheet_id).worksheet(worksheet)
    values = sheet.get_all_values()
    # app.logger.info(values)
    return values


def insert_sheet_data(spreadsheet_id: str, row: list) -> bool:
    """
    Registers an appointment with the veterinarian
    """

    try:
        sheet = client.open_by_key(spreadsheet_id).worksheet('Citas_agendadas')
        # Set row values to insert
        sheet.append_row(row)
        # app.logger.info(f'Data saved: {row}')
        return True  # Register successfully
    except:
        #app.logger.error(f'Error saving data: {row}')
        return False  # Error register
    
def insert_sheet_data_schedule(spreadsheet_id: str, row: list) -> bool:
    """
    Registers an appointment with the veterinarian
    """

    try:
        sheet = client.open_by_key(spreadsheet_id).worksheet('Horarios')
        # Set row values to insert
        sheet.append_row(row)
        # app.logger.info(f'Data saved: {row}')
        return True  # Register successfully
    except:
        #app.logger.error(f'Error saving data: {row}')
        return False  # Error register
    
def delete_sheet_data(spreadsheet_id: str, row_index: int,worksheet: str) -> bool:
    """
    Delete a row from the spreadsheet.

    Args:
        spreadsheet_id: The ID of the spreadsheet.
        row_index: The index of the row to be deleted (0-based).

    Returns:
        True if the row was deleted successfully, False otherwise.
    """
    try:
        sheet = client.open_by_key(spreadsheet_id).worksheet(worksheet)
        sheet.delete_row(row_index + 1)  # Adjust row index (1-based in Google Sheets)
        return True
    except Exception as e:
        # Handle exceptions appropriately (e.g., logging, error handling)
        return False