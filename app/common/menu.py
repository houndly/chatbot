"""
	Validate menu option selected by user and process information
	based on the option

	Possible options:
		CHECK_APPOINTMENTS: Check upcoming appointments
		NEW_APPOINTMENT: Set new appointment
"""

from app.common.constants import MenuOptions

# FIXME: Validate and make corrections
def handle_menu(number):
    switcher = {
        MenuOptions.CHECK_APPOINTMENTS: "1.",
        MenuOptions.NEW_APPOINTMENT: "2."
    }

    return ""