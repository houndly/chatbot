"""
Validate menu option selected by user and process information
based on the option

Possible options:
	CHECK_APPOINTMENTS: Check upcoming appointments
	NEW_APPOINTMENT: Set new appointment
"""

from twilio.twiml.messaging_response import MessagingResponse
from app.appointment import get_appointments
from app.common.constants import CHECK_APPOINTMENTS, NEW_APPOINTMENT


def handle_menu(incoming_msg: str) -> str:
	response = MessagingResponse() # Twilio response object

	if incoming_msg not in [CHECK_APPOINTMENTS, NEW_APPOINTMENT]:
		response.message("Hola, gracias por escribirnos. Empecemos eligiendo una opción del menú: \n 1. Consultar citas \n 2. Agendar cita")
		return str(response)

	if incoming_msg == CHECK_APPOINTMENTS:
		return ask_for_user_id(response)

	if incoming_msg == NEW_APPOINTMENT:
		return ask_for_appointment_data


def ask_for_user_id(message_response: MessagingResponse) -> str:
	"""
	Ask for user ID to search information based on this data
	"""
	appointments = get_appointments()
	message_response.message("Estas son tus citas: ")

	for appointment in appointments:
		message_response.message(appointment.get_appointment_info())

	return str(message_response)


def ask_for_appointment_data() -> str:
	"""
	Ask for data to add into new appointment
	"""
	return "Hola mundo"