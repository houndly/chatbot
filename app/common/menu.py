"""
Validate menu option selected by user and process information
based on the option

Possible options:
	CHECK_APPOINTMENTS: Check upcoming appointments
	NEW_APPOINTMENT: Set new appointment
"""

from twilio.twiml.messaging_response import MessagingResponse
from app.appointment import get_appointments, register_appointment
from app.common.constants import CHECK_APPOINTMENTS, NEW_APPOINTMENT
from app.appointment.appointment import Appointment
from app.appointment.constants import APPOINTMENTS_SHEET_ID
from app.appointment.constants import AppointmentStateType

user_state = {}


def handle_menu(incoming_msg: dict[str, str]) -> str:
    response = MessagingResponse()  # Twilio response object
    body: str = incoming_msg.get("Body").lower()
    from_number: str = incoming_msg.get("WaId")
    if "new_appointment_state" in user_state:
        return ask_for_appointment_data(response, body, from_number)

    if body not in [CHECK_APPOINTMENTS, NEW_APPOINTMENT]:
        response.message(
            "Hola, gracias por escribirnos. Empecemos eligiendo una opción del menú: \n 1. Consultar citas \n 2. Agendar cita"
        )
    elif body == CHECK_APPOINTMENTS:
        return ask_for_user_id()

    elif body == NEW_APPOINTMENT:

        user_state["new_appointment_state"] = "ask_name"
        response.message("Vamos a agendar una nueva cita. ¿Cuál es tu nombre?")

    return str(response)


def ask_for_user_id() -> str:
    """
    Ask for user ID to search information based on this data
    """
    response = MessagingResponse()
    appointments = get_appointments()
    if appointments:
        response.message("Estas son tus citas: ")

        for appointment in appointments:
            response.message(appointment.get_appointment_info())

    return str(response)


def ask_for_appointment_data(message_response: MessagingResponse, body: str, from_number: str) -> str:
    """
    Ask for data to add into new appointment
    """
    if user_state["new_appointment_state"] == "ask_name":
        user_state["new_appointment_state"] = "ask_pet_name"
        user_state["name"] = body
        message_response.message("¿Cuál es el nombre de tu mascota?")
    elif user_state["new_appointment_state"] == "ask_pet_name":
        user_state["new_appointment_state"] = "ask_document_id"
        user_state["pet_name"] = body
        message_response.message("¿Cuál es tu número de documento?")
    elif user_state["new_appointment_state"] == "ask_document_id":
        user_state["new_appointment_state"] = "ask_date"
        user_state["document_id"] = body
        message_response.message(
            "¿En qué fecha quieres la cita? \n(dd/mm/aaaa)"
        )
    elif user_state["new_appointment_state"] == "ask_date":
        user_state["new_appointment_state"] = None
        user_state["appointment_date"] = body
        message_response.message("¿A qué hora? \n(hh:mm)")
    else:
        user_state["appointment_time"] = body
        user_state["phone"] = from_number
        appointment = Appointment(
            owner_name=user_state["name"],
            pet_name=user_state["pet_name"],
            phone=user_state["phone"],
            document_id=user_state["document_id"],
            date=user_state["appointment_date"],
            appointment_time=user_state["appointment_time"],
            state="Pendiente"
        )
        is_registered = register_appointment(appointment, APPOINTMENTS_SHEET_ID)
        if is_registered:
            message_response.message("¡Gracias! Hemos agendado tu cita.")
        else:
            message_response.message(
                "¡Ups! Algo salió mal. Intenta de nuevo más tarde."
            )
    return str(message_response)
