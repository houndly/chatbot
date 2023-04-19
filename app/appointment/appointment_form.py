"""
Entity to handle appointment state when user want to create a new one

Properties here allow to us to know which data is missing and what is necessary to
ask user in order to create a new appointment
"""
from dataclasses import dataclass
from app.appointment.appointment import Appointment
from app.appointment.constants import PENDING


@dataclass
class AppointmentForm:
    """
    Appointment Form entity class
    """

    asked_owner_name: bool = False
    asked_pet_name: bool = False
    asked_document_id: bool = False
    asked_date: bool = False
    asked_time: bool = False
    is_handle_new_appointment: bool = False
    appointment: Appointment = Appointment()  # Appointment to handle data

    def is_complete_data(self) -> bool:
        """
        Validate if data is missing and return False if is necessary to ask more information
        If user complete all the data, return True indicating information for appointment is complete
        """

        if self.asked_owner_name and self.asked_pet_name and self.asked_document_id and self.asked_date and self.asked_time:
            return True
        # If information is missing, ask for more information
        return False

    def set_data_message(self, information: str):
        """
        Set data of the new appointment based on information missing

        For example if we don't have pet information, means user get us name information
        so we can set this information into Appointment.owner_name property

        Parameters:
            information: Means information getting by user on WhatsApp
        """

        if not self.asked_owner_name:
            self.appointment.phone = information
        elif not self.asked_pet_name:
            self.appointment.owner_name = information
        elif not self.asked_document_id:
            self.appointment.pet_name = information
        elif not self.asked_date:
            self.appointment.document_id = information
        elif not self.asked_time:
            self.appointment.date = information
        # Final information asked is time of the appointment
        self.appointment.appointment_time = information
        # New appintments always are PENDING by default
        self.appointment.state = PENDING

    def get_state_message(self) -> str:
        """
        Get the valid message to ask user based on information missing
        """

        if not self.asked_owner_name:
            self.asked_owner_name = True
            return '¿Cuál es tu nombre?'
        elif not self.asked_pet_name:
            self.asked_pet_name = True
            return '¿Cuál es el nombre de tu mascota?'
        elif not self.asked_document_id:
            self.asked_document_id = True
            return '¿Cuál es tu número de documento?'
        elif not self.asked_date:
            self.asked_date = True
            return '¿En qué fecha quieres la cita? \n(dd/mm/aaaa)'
        elif not self.asked_time:
            self.asked_time = True
            return '¿A qué hora? \n(hh:mm)'
        return ''  # Empty means all values are completed
