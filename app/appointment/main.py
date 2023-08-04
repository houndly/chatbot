from app.appointment.appointment_model import AppointmentModel
from app.appointment.constants import APPOINTMENTS_SHEET_ID
from app.common.sheets import get_sheet_data, insert_sheet_data, delete_sheet_data
import app.common.constants as cm


def register_appointment(
    sheet_id: str,
    user_session: dict
) -> bool:
    """
    Registers an appointment with the veterinarian
    """

    appointment = session_to_appointment(user_session)
    # Set row values to insert
    new_row = appointment.get_data_to_row()

    is_register = insert_sheet_data(sheet_id, new_row)

    return is_register  # New appointment register successfully or not


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


def get_appointments(from_number: str) -> list[AppointmentModel]:
    """
    Get all appointments from the given spreadsheet.

    Returns:
        A list of dictionaries containing the appointments.
    """
    data = get_sheet_data(APPOINTMENTS_SHEET_ID)
    data = data[3:]  # Remove the header and the first empty row

    appointments = []
    for row in data:
        if from_number == row[cm.PHONE_COLUMN_ORDER]:  # Missing colon (:) here
            print(from_number)
            new_appointment = AppointmentModel(
                id=row[cm.ID_COLUMN_ORDER], 
                owner_name=row[cm.OWNER_NAME_COLUMN_ORDER],
                pet_name=row[cm.PET_NAME_COLUMN_ORDER],
                appointment_time=row[cm.TIME_COLUMN_ORDER],
                date=row[cm.DATE_COLUMN_ORDER],
                phone=row[cm.PHONE_COLUMN_ORDER],
                document_id=row[cm.DOCUMENT_COLUMN_ORDER],
                state=row[cm.STATE_COLUMN_ORDER],
                type=row[cm.TYPE_COLUMN_ORDER]
            )
            appointments.append(new_appointment)

    return appointments

def delete_appointment_by_id(appointment_id: str) -> bool:
    """
    Delete an appointment by its ID from the spreadsheet.
    Return True if the appointment is found and deleted, False otherwise.
    """

    data = get_sheet_data(APPOINTMENTS_SHEET_ID)
    data = data[3:]  # Remove the header and the first empty row

    for index, row in enumerate(data):
        if appointment_id == row[cm.ID_COLUMN_ORDER]:
            # Delete the row corresponding to the appointment_id
            delete_sheet_data(APPOINTMENTS_SHEET_ID, index + 3)  # Add 3 to account for the header and the removed empty row
            return True  # Return True if the appointment is found and deleted

    return False  #