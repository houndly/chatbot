"""
Validate menu option selected by user and process information
based on the option

Possible options:
	CHECK_APPOINTMENTS: Check upcoming appointments
	NEW_APPOINTMENT: Set new appointment
"""

from twilio.twiml.messaging_response import MessagingResponse
from app.appointment.appointment_form import AppointmentForm
from app.appointment.constants import APPOINTMENTS_SHEET_ID
from app.appointment.main import get_appointments, register_appointment
from app.commerce.commerce_model import CommerceModel
from app.commerce.main import get_commerce_data
from app.common.constants import CHECK_APPOINTMENTS, NEW_APPOINTMENT


# Data of the commerce
commerce_data: CommerceModel = None
# Instance for handle Appointment form
appointment_form: AppointmentForm = None
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

    # TODO: Add commerce ID from request
    # FOR TEST PURPOSE, THIS VALUE CAN'T BE NULL OR EMPTY
    _validate_commerce_data("12345")

    if continue_chat:
        continue_chat = False
        if body == 'y':
            response.message(commerce_data.messages.initial_msg)
            return str(response)
        elif body == 'n':
            response.message(commerce_data.messages.good_bye_msg)
            return str(response)
        else:
            response.message(commerce_data.messages.error_msg)
            return str(response)

    elif appointment_form.is_handle_new_appointment:
        return ask_for_appointment_data(response, body)

    elif body not in [CHECK_APPOINTMENTS, NEW_APPOINTMENT]:
        response.message(commerce_data.messages.initial_msg)
        return str(response)

    elif body == CHECK_APPOINTMENTS:
        return _ask_for_user_id(response)

    elif body == NEW_APPOINTMENT:
        appointment_form.is_handle_new_appointment = True
        appointment_form.set_data_message(from_number)  # Set user number
        response.message(commerce_data.messages.new_appointment_msg)
        return ask_for_appointment_data(response, body)

    return str(commerce_data.messages.error_msg)


def _validate_commerce_data(commerce_id: str):
    """
        Validate which commerce data is necessary to show user based oin the commerce
        identifier came in the request (Normally this data it will be the phone number from Twilio)
    """
    global commerce_data, appointment_form

    # If commerce set in the form is different to the last commerce
    # Set the new one from service
    if ((commerce_data is None) or (appointment_form.commerce.commerce_id != commerce_id)):
        commerce_data = get_commerce_data(commerce_id)
        appointment_form = AppointmentForm(commerce=commerce_data)


def _ask_for_user_id(message_response: MessagingResponse) -> str:
    """
    Ask for user ID to search information based on this data
    """

    appointments = get_appointments()
    if appointments:
        message_response.message(
            commerce_data.messages.current_appointments_msg)

        for appointment in appointments:
            message_response.message(appointment.get_appointment_info())

        _ask_for_more_process(message_response)

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
            message_response.message(
                commerce_data.messages.appointment_added_msg)
            _ask_for_more_process(message_response)

        else:
            message_response.message(commerce_data.messages.error_msg)
    else:
        message_response.message(message_to_show)

    return str(message_response)


def _ask_for_more_process(message_response: MessagingResponse) -> str:
    """
    Ask user if it is necessary to continue showing the menu
    """
    global continue_chat

    continue_chat = True
    message_response.message(commerce_data.messages.continue_chat_msg)
    return str(message_response)
