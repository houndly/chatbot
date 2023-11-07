"""
Validate menu option selected by user and process information
based on the option

Possible options:
	CHECK_APPOINTMENTS: Check upcoming appointments
	NEW_APPOINTMENT: Set new appointment
"""

from flask import session
from twilio.twiml.messaging_response import MessagingResponse
from app.appointment.schedule_model import ScheduleModel
from app.appointment.appointment_form import AppointmentForm
from app.appointment.mapper import session_to_schedule
from app.appointment.constants import APPOINTMENTS_SHEET_ID
from app.appointment.main import get_appointments, register_appointment, delete_appointment_by_id,delete_shedule_by_id, register_appointment_schedule, get_schedules
from app.commerce.commerce_model import CommerceModel
from app.commerce.main import get_commerce_data
from app.common.constants import CHECK_APPOINTMENTS, NEW_APPOINTMENT, DELETE_APPOINTMENT
from app import app


# Data of the commerce
commerce_data: CommerceModel = None
# Instance for handle Appointment form


def handle_menu(incoming_msg: dict[str, str]):
    """
    Handle menu options based on user process
    """

    response = MessagingResponse()  # Twilio response object
    body: str = incoming_msg.get("Body").lower()
    from_number: str = incoming_msg.get("WaId")
    # Get session object
    user_session = session.get(from_number, {})

    #user_session.clear()

    if not user_session:
        user_session["continue_chat"] = False
    # TODO: Add commerce ID from request
    # FOR TEST PURPOSE, THIS VALUE CAN'T BE NULL OR EMPTY
    _validate_commerce_data("12345")
    # app.logger.info(user_session)

    if user_session.get("appointment_form") and user_session.get("appointment_form").get("is_handle_new_appointment"):
        if user_session.get("appointment_form").get("appointment") and user_session.get("appointment_form").get("appointment").get("date") != None and user_session.get("appointment_form").get("appointment").get("appointment_time") != None:
            if not is_datetime_available(session_to_schedule(user_session.get("appointment_form").get("appointment"))):
                appointment_form.is_handle_new_appointment = True
                appointment_form.asked_date = False
                appointment_form.asked_time = False
                appointment_form.asked_type = False
                user_session["appointment_form"]["appointment_questions"]["asked_date"] = False
                user_session["appointment_form"]["appointment_questions"]["asked_time"] = False
                user_session["appointment_form"]["appointment_questions"]["asked_type"] = False
                user_session["appointment_form"]["appointment"]["date"] = None
                user_session["appointment_form"]["appointment"]["appointment_time"] = None
                user_session["appointment_form"]["appointment"]["type"] = None
                user_session["is_date_unavailable"] = True
            else:
                user_session["is_date_unavailable"] = False
        else:
            user_session["is_date_unavailable"] = False

                # return str(response)
 
        
    if user_session["continue_chat"]:
        user_session["continue_chat"] = False
        session[from_number] = user_session
        if body == 'si':
            response.message(commerce_data.messages.initial_msg)
            return str(response)
        elif body == 'no':
            response.message(commerce_data.messages.good_bye_msg)
            user_session.clear()
            session[from_number] = user_session
            return str(response)
        else:
            response.message(commerce_data.messages.error_msg)
            return str(response)

  
    elif user_session.get("appointment_form") and user_session.get("appointment_form").get("is_handle_new_appointment"):
        if user_session.get("is_date_unavailable"):
            response.message(commerce_data.messages.appointment_shedule_err_msg)
        return ask_for_appointment_data(response, body, from_number)

    elif user_session.get("delete_appointment"):
        user_session["delete_appointment"] = False
        if delete_appointment_by_id(body) and delete_shedule_by_id(body):
            response.message(
                commerce_data.messages.appointment_delete_success_msg)
        else:
            response.message(commerce_data.messages.appointment_delete_err_msg)

        _ask_for_more_process(response, user_session, from_number)

        return str(response)

    elif body not in [CHECK_APPOINTMENTS, NEW_APPOINTMENT, DELETE_APPOINTMENT]:
        response.message(commerce_data.messages.initial_msg)
        user_session.clear()
        session[from_number] = user_session
        return str(response)

    elif body == CHECK_APPOINTMENTS:
        return _ask_for_user_id(response, user_session, from_number)

    elif body == NEW_APPOINTMENT:
        appointment_form.is_handle_new_appointment = True
        form = user_session["appointment_form"] = appointment_form.to_dict()
        appointment_form.set_data_message(
            from_number=from_number, user_session=form
        )  # Set user number
        response.message(commerce_data.messages.new_appointment_msg)
        session[from_number] = user_session
        return ask_for_appointment_data(response, body, from_number)

    elif body == DELETE_APPOINTMENT:
        return _ask_delete_appointment(response, user_session, from_number)

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


def _ask_for_user_id(message_response: MessagingResponse, user_session: dict, from_number: str) -> str:
    """
    Ask for user ID to search information based on this data
    """
    appointments = get_appointments(from_number)
    if appointments:
        message_response.message(
            commerce_data.messages.current_appointments_msg)

        for appointment in appointments:
            message_response.message(appointment.get_appointment_info())
    else:
        message_response.message(
            commerce_data.messages.appointment_pending_msg)

    _ask_for_more_process(message_response, user_session, from_number)

    return str(message_response)


def _ask_delete_appointment(message_response: MessagingResponse, user_session: dict, from_number: str) -> str:

    appointments = get_appointments(from_number)
    if appointments:
        message_response.message(
            commerce_data.messages.current_appointments_msg)

        for appointment in appointments:
            message_response.message(appointment.get_appointment_info())
        message_response.message(commerce_data.messages.appointment_delete_msg)
        user_session["delete_appointment"] = True
        session[from_number] = user_session
    else:
        message_response.message(
            commerce_data.messages.appointment_pending_msg)
        _ask_for_more_process(message_response, user_session, from_number)

    return str(message_response)


def ask_for_appointment_data(message_response: MessagingResponse, body: str, from_number: str) -> str:
    """
    Ask for data to save a new appointment
    """

    # Get session object
    user_session = session.get(from_number, {})
    form = user_session["appointment_form"]
    if not appointment_form.is_complete_data(user_session=form["appointment_questions"]):
        is_valid_input = appointment_form.validate_input(
            body, form["appointment_questions"])
        if not is_valid_input:
            message_response.message(commerce_data.messages.format_error_msg)
            return str(message_response)
    appointment_form.set_data_message(
        from_number=from_number, user_session=form, information=body
    )
    message_to_show = appointment_form.get_state_message(
        user_session=form["appointment_questions"])
    if (message_to_show == '' and appointment_form.is_complete_data(user_session=form["appointment_questions"])):
        appointment_form.reset_form_state(
            user_session=form)  # Reset values from form
        is_registered = register_appointment(
            APPOINTMENTS_SHEET_ID,
            form["appointment"]
        )
        
        is_registered_schedule = register_appointment_schedule(
                    APPOINTMENTS_SHEET_ID,
                    form["appointment"]
                )
        if is_registered and  is_registered_schedule:
            message_response.message(
                commerce_data.messages.appointment_added_msg
            )
            _ask_for_more_process(message_response, user_session, from_number)

        else:
            message_response.message(commerce_data.messages.error_msg)

        user_session.pop("appointment_form", None)
        session[from_number] = user_session

    else:
        message_response.message(message_to_show)
        # Update user session with current state of appointment_form
        session[from_number] = user_session

    return str(message_response)


def _ask_for_more_process(message_response: MessagingResponse, user_session: dict, from_number: str) -> str:
    """
    Ask user if it is necessary to continue showing the menu
    """

    user_session["continue_chat"] = True
    session[from_number] = user_session
    message_response.message(commerce_data.messages.continue_chat_msg)
    return str(message_response)

def is_datetime_available(scheduleModel:ScheduleModel ) -> bool:
    """
    Check if the given date and time are available in the schedule.
    """
    schedule =  get_schedules()
    for entry in schedule:
        if (entry.date == scheduleModel.date and entry.time_init == scheduleModel.time_init and entry.time_end == scheduleModel.time_end):
            return False  # The date and time are already scheduled
    return True  # The date and time are available
