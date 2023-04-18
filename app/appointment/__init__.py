import app.common.constants as common_constants
from app.appointment.appointment import Appointment
from app.appointment.constants import APPOINTMENTS_SHEET_ID, AppointmentStateType
from app.common.sheets import get_data, insert_data


def register_appointment(appointment: Appointment, sheet_id: str) -> bool:
	"""
 	Registers an appointment with the veterinarian
  """
	# Set row values to insert
	new_row = appointment.get_data_to_row()

	is_register = insert_data(sheet_id, new_row)

	return is_register # New appointment register successfully or not


def get_appointments() -> list[Appointment]:
	"""
	Get all appointments from the given spreadsheet.

	Returns:
		A list of dictionaries containing the appointments.
	"""
	data = get_data(APPOINTMENTS_SHEET_ID)
	data = data[3:] # Remove the header and the first empty row

	appointments = list[Appointment]()
	for row in data:
		new_appointment = Appointment(
			owner_name=row[common_constants.OWNER_NAME_COLUMN_ORDER],
			pet_name=row[common_constants.PET_NAME_COLUMN_ORDER],
			appointment_time=row[common_constants.TIME_COLUMN_ORDER],
			date=row[common_constants.DATE_COLUMN_ORDER],
			phone=row[common_constants.PHONE_COLUMN_ORDER],
			document_id=row[common_constants.DOCUMENT_COLUMN_ORDER],
			state='test' # Modify using data from Sheets
			
		)
		appointments.append(new_appointment)

	return appointments