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
