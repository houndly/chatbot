from app.appointment.appointment_model import AppointmentModel
from app.appointment.constants import APPOINTMENTS_SHEET_ID
from app.common.sheets import get_sheet_data, insert_sheet_data
import app.common.constants as cm


def register_appointment(appointment: AppointmentModel, sheet_id: str) -> bool:
    """
    Registers an appointment with the veterinarian
    """

    # Set row values to insert
    new_row = appointment.get_data_to_row()

    is_register = insert_sheet_data(sheet_id, new_row)

    return is_register  # New appointment register successfully or not


def get_appointments() -> list[AppointmentModel]:
    """
    Get all appointments from the given spreadsheet.

    Returns:
        A list of dictionaries containing the appointments.
    """
    data = get_sheet_data(APPOINTMENTS_SHEET_ID)
    data = data[3:]  # Remove the header and the first empty row

    appointments = list[AppointmentModel]()
    for row in data:
        new_appointment = AppointmentModel(
            owner_name=row[cm.OWNER_NAME_COLUMN_ORDER],
            pet_name=row[cm.PET_NAME_COLUMN_ORDER],
            appointment_time=row[cm.TIME_COLUMN_ORDER],
            date=row[cm.DATE_COLUMN_ORDER],
            phone=row[cm.PHONE_COLUMN_ORDER],
            document_id=row[cm.DOCUMENT_COLUMN_ORDER],
            state=row[cm.STATE_COLUMN_ORDER]
        )
        appointments.append(new_appointment)

    return appointments
