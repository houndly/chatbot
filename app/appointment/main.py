from app.appointment.constants import APPOINTMENTS_SHEET_ID, ID_APPOINTMENTS_SHEET, ID_SCHEDULES_SHEET
from app.appointment.schedule_model import ScheduleModel
from app.appointment.appointment_model import AppointmentModel
from app.common.sheets import get_sheet_data, insert_sheet_data, delete_sheet_data, insert_sheet_data_schedule
import app.common.constants as cm
from app.appointment.mapper import session_to_appointment,session_to_schedule
from app import app


def register_appointment(sheet_id: str,user_session: dict) -> bool:
    """
    Registers an appointment with the veterinarian
    """

    appointment = session_to_appointment(user_session)
    # Set row values to insert
    new_row = appointment.get_data_to_row()

    is_register = insert_sheet_data(sheet_id, new_row)

    return is_register  # New appointment register successfully or not


def register_appointment_schedule(sheet_id: str,user_session: dict) -> bool:
    """
    Registers an appointment with the veterinarian
    """
    schedule = session_to_schedule(user_session)
    # Set row values to insert
    new_row = schedule.get_data_to_row()
    is_register = insert_sheet_data_schedule(sheet_id, new_row)

    return is_register  # New appointment register successfully or not


def get_appointments(from_number: str) -> list[AppointmentModel]:
    """
    Get all appointments from the given spreadsheet.

    Returns:
        A list of dictionaries containing the appointments.
    """
    data = get_sheet_data(APPOINTMENTS_SHEET_ID, ID_APPOINTMENTS_SHEET)
    data = data[3:]  # Remove the header and the first empty row

    appointments = []
    for row in data:
        if from_number == row[cm.PHONE_COLUMN_ORDER]:  # Missing colon (:) here
            new_appointment = AppointmentModel(
                id=row[cm.ID_COLUMN_ORDER], 
                owner_name=row[cm.OWNER_NAME_COLUMN_ORDER],
                pet_name=row[cm.PET_NAME_COLUMN_ORDER],
                appointment_time=row[cm.TIME_COLUMN_ORDER],
                date=row[cm.DATE_COLUMN_ORDER],
                phone=row[cm.PHONE_COLUMN_ORDER],
                type=row[cm.TYPE_COLUMN_ORDER],
                state=row[cm.STATE_COLUMN_ORDER]
            )
            appointments.append(new_appointment)

    return appointments


def get_schedules() -> list[ScheduleModel]:
    """
    Get all appointments from the given spreadsheet.

    Returns:
        A list of dictionaries containing the appointments.
    """
    data = get_sheet_data(APPOINTMENTS_SHEET_ID, 'Horarios')
    data = data[3:]  # Remove the header and the first empty row

    schedules = []
    for row in data:
        new_schedule = ScheduleModel(
            id=row[cm.ID_SCHEDULE_COLUMN_ORDER], 
            date=row[cm.DATE_SCHEDULE_COLUMN_ORDER],
            time_init=row[cm.DATE_INIT__SCHEDULE_COLUMN_ORDER],
            time_end=row[cm.DATE_END_SCHEDULE_COLUMN_ORDER]
        )
        schedules.append(new_schedule)

    return schedules

def delete_appointment_by_id(appointment_id: str) -> bool:
    """
    Delete an appointment by its ID from the spreadsheet.
    Return True if the appointment is found and deleted, False otherwise.
    """

    data = get_sheet_data(APPOINTMENTS_SHEET_ID, ID_APPOINTMENTS_SHEET)
    data = data[3:]  # Remove the header and the first empty row

    for index, row in enumerate(data):
        if appointment_id == row[cm.ID_COLUMN_ORDER]:
            # Delete the row corresponding to the appointment_id
            delete_sheet_data(APPOINTMENTS_SHEET_ID, index + 3,ID_APPOINTMENTS_SHEET)  # Add 3 to account for the header and the removed empty row
            return True  # Return True if the appointment is found and deleted

    return False  #

def delete_shedule_by_id(shedule_id: str) -> bool:
    """
    Delete an shedule by its ID from the spreadsheet.
    Return True if the shedule is found and deleted, False otherwise.
    """

    data = get_sheet_data(APPOINTMENTS_SHEET_ID, ID_SCHEDULES_SHEET)
    data = data[3:]  # Remove the header and the first empty row

    for index, row in enumerate(data):
        if shedule_id == row[cm.ID_SCHEDULE_COLUMN_ORDER]:
            # Delete the row corresponding to the shedule_id
            delete_sheet_data(APPOINTMENTS_SHEET_ID, index + 3,ID_SCHEDULES_SHEET)  # Add 3 to account for the header and the removed empty row
            return True  # Return True if the shedule is found and deleted

    return False  #