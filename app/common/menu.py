"""
Validate menu option selected by user and process information
based on the option

Possible options:
	CHECK_APPOINTMENTS: Check upcoming appointments
	NEW_APPOINTMENT: Set new appointment
"""

from twilio.twiml.messaging_response import MessagingResponse
from app.appointment import get_appointments, register_appointment
from app.appointment.appointment_form import AppointmentForm
from app.common.constants import CHECK_APPOINTMENTS, NEW_APPOINTMENT
from app.appointment.constants import APPOINTMENTS_SHEET_ID


# Instance for handle Appointment form
appointment_form: AppointmentForm = AppointmentForm()
# Initial menu message
initial_msg: str = "Hola, gracias por escribirnos. Empecemos eligiendo una opción del menú: \n 1. Consultar citas \n 2. Agendar cita"
# Error message
error_msg: str = "¡Ups! Algo salió mal. Intenta de nuevo más tarde."
# Indicates user finished his task and is available con continue again with chat
continue_chat: bool = False


def handle_menu(incoming_msg: dict[str, str]):
    """
    Handle menu options based on user process
    """
    global continue_chat

    response = MessagingResponse()  # Twilio response object
    body: str = incoming_msg.get("Body").lower()
    from_number: str = incoming_msg.get("WaId")

    if continue_chat:
        continue_chat = False
        if body.lower() == 'y':
            return str(response.message(initial_msg))
        elif body.lower() == 'n':
            return str(response.message("Gracias por preferirnos !"))
        else:
            return str(response.message(error_msg))

    elif appointment_form.is_handle_new_appointment:
        return ask_for_appointment_data(response, body)

    elif body not in [CHECK_APPOINTMENTS, NEW_APPOINTMENT]:
        return str(response.message(initial_msg))

    elif body == CHECK_APPOINTMENTS:
        return ask_for_user_id(response)

    elif body == NEW_APPOINTMENT:
        appointment_form.is_handle_new_appointment = True
        appointment_form.set_data_message(from_number)  # Set user number
        response.message("Vamos a agendar una nueva cita")
        return ask_for_appointment_data(response, body)

    return str(error_msg)


def ask_for_user_id(message_response: MessagingResponse) -> str:
    """
    Ask for user ID to search information based on this data
    """

    appointments = get_appointments()
    if appointments:
        message_response.message("Estas son tus citas: ")

        for appointment in appointments:
            message_response.message(appointment.get_appointment_info())

        ask_for_more_process(message_response)

    return str(message_response)


def ask_for_appointment_data(message_response: MessagingResponse, body: str) -> str:
    """
    Ask for data to save a new appointment
    """

    appointment_form.set_data_message(body)
    message_to_show = appointment_form.get_state_message()

    if (message_to_show == '' and appointment_form.is_complete_data()):
        appointment_form.is_handle_new_appointment = False  # Appointment data handle
        is_registered = register_appointment(
            appointment_form.appointment, APPOINTMENTS_SHEET_ID)

        if is_registered:
            message_response.message("¡Gracias! Hemos agendado tu cita.")
            ask_for_more_process(message_response)

        else:
            message_response.message(error_msg)
    else:
        message_response.message(message_to_show)

    return str(message_response)


def ask_for_more_process(message_response: MessagingResponse) -> str:
    """
    Ask user if it is necessary to continue shwoing the menu
    """
    global continue_chat

    continue_chat = True
    message_response.message(
        "Indicanos si deseas continuar chateando con nosotros (Y/n)")
    return str(message_response)
