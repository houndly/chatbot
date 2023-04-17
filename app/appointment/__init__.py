from app.appointment.appointment import Appointment
from app.common.sheets import getConnection as sheets

def register_appointment(appointment: Appointment) -> bool:
	"""
 	Registers an appointment with the veterinarian
  """
	# Set row values to insert
	new_row = appointment.get_data_to_row()

	is_register = sheets.insert_data(new_row)

	return is_register # New appointment register successfully