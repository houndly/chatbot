from app.appointment.appointment_form import AppointmentForm
from app.appointment.appointment_model import AppointmentModel
from app.appointment.schedule_model import ScheduleModel
from datetime import datetime
from app import app
import re


appointment_form: AppointmentForm = None


def session_to_appointment(user_session: dict) -> AppointmentModel:
    """
    Transform user session to appointment
    """
    return AppointmentModel(
        id=user_session.get("id"),
        owner_name=user_session.get("owner_name"),
        pet_name=user_session.get("pet_name"),
        appointment_time=user_session.get("appointment_time"),
        date=user_session.get("date"),
        phone=user_session.get("phone"),
        document_id=user_session.get("document_id"),
        state=user_session.get("state"),
        type=user_session.get("type")
    )




def session_to_schedule(user_session: dict) -> ScheduleModel:
    """
    Transform user session to schedule
    """
    app.logger.info(user_session)
    appointment_time = user_session.get("appointment_time")

    # Split the appointment_time into time_init and time_end
    time_init_str, time_end_str = appointment_time.split(" -> ")

    # Extract the time part using regular expression
    time_regex = r'\b\d{1,2}:\d{2}\b'
    time_init_str = re.search(time_regex, time_init_str.strip()).group()
    time_end_str = re.search(time_regex, time_end_str.strip()).group()

    # Parse the time parts into time objects
    time_init = datetime.strptime(time_init_str, "%H:%M").time()
    time_end = datetime.strptime(time_end_str, "%H:%M").time()

    # Convert time objects back to strings
    time_init_str = time_init.strftime("%H:%M")
    time_end_str = time_end.strftime("%H:%M")

    return ScheduleModel(
        id=str(user_session.get("id")),
        date=str(user_session.get("date")),
        time_init=time_init_str,
        time_end=time_end_str,
    )