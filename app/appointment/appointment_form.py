"""
Entity to handle appointment state when user want to create a new one

Properties here allow to us to know which data is missing and what is necessary to
ask user in order to create a new appointment
"""
from dataclasses import dataclass
from app.appointment.appointment_model import AppointmentModel
from app.appointment.constants import PENDING
from app.commerce.commerce_model import CommerceModel


@dataclass
class AppointmentForm:
    """
    Appointment Form entity class
    """

    def __init__(self, commerce: CommerceModel):
        self.commerce = commerce

    asked_owner_name: bool = False
    asked_pet_name: bool = False
    asked_document_id: bool = False
    asked_date: bool = False
    asked_time: bool = False
    is_handle_new_appointment: bool = False
    appointment: AppointmentModel = AppointmentModel()  # Appointment to handle data
    commerce: CommerceModel = CommerceModel()  # Commerce data to handle in the form

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
        else:
            self.appointment.appointment_time = information
            # New appointments always are PENDING by default
            self.appointment.state = PENDING

    def get_state_message(self) -> str:
        """
        Get the valid message to ask user based on information missing
        """

        if not self.asked_owner_name:
            self.asked_owner_name = True
            return self.commerce.messages.user_name_msg
        elif not self.asked_pet_name:
            self.asked_pet_name = True
            return self.commerce.messages.pet_name_msg
        elif not self.asked_document_id:
            self.asked_document_id = True
            return self.commerce.messages.document_id_msg
        elif not self.asked_date:
            self.asked_date = True
            return self.commerce.messages.appointment_date_msg
        elif not self.asked_time:
            self.asked_time = True
            return self.commerce.messages.appointment_time_msg
        return ''  # Empty means all values are completed

    def reset_form_state(self):
        """
        Reset form state to validate new appointments
        """
        self.asked_owner_name = False
        self.asked_pet_name = False
        self.asked_document_id = False
        self.asked_date = False
        self.asked_time = False
        self.is_handle_new_appointment = False
