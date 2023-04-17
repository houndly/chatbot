"""
	Validate menu option selected by user and process information
	based on the option

	Possible options:
		CHECK_APPOINTMENTS: Check upcoming appointments
		NEW_APPOINTMENT: Set new appointment
"""

from app.common.constants import MenuOptions

def handle_menu(number):
    switcher = {
        MenuOptions.CHECK_APPOINTMENTS: ask_for_user_id,
        MenuOptions.NEW_APPOINTMENT: ask_for_appointment_data
    }

    option = switcher.get(number)
    return option

def ask_for_user_id():
	"""
	Ask for user ID to search information based on this data
 	"""
	return "Hola mundo"

def ask_for_appointment_data():
	"""
	Ask for data to add into new appointment
	"""
	return "Hola mundo"