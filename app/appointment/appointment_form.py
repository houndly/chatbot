"""
Entity to handle appointment state when user want to create a new one

Properties here allow to us to know which data is missing and what is necessary to
ask user in order to create a new appointment
"""
from dataclasses import dataclass
from app.appointment.appointment_model import AppointmentModel
from app.appointment.constants import PENDING
from app.commerce.commerce_model import CommerceModel
import datetime
import random


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
    asked_type: bool = False
    is_handle_new_appointment: bool = False
    appointment: AppointmentModel = AppointmentModel()  # Appointment to handle data
    commerce: CommerceModel = CommerceModel()  # Commerce data to handle in the form

    def is_complete_data(self, user_session: dict) -> bool:
        """
        Validate if data is missing and return False if is necessary to ask more information
        If user complete all the data, return True indicating information for appointment is complete
        """
        if all(user_session.values()):
            return True
        # If information is missing, ask for more information
        return False

    def set_data_message(self, from_number: str, user_session: dict, information: str = None):
        """
        Set data of the new appointment based on information missing

        For example if we don't have pet information, means user get us name information
        so we can set this information into Appointment.owner_name property

        Parameters:
            information: Means information getting by user on WhatsApp
        """
        form: dict = user_session["appointment_questions"]  # only the questions dict
        type_mapping = {
                "1": "Baño y Aseo",
                "2": "Consulta Médica",
                "3": "Vacunación",
                "4": "Otros"
            }
        
        if not form.get("asked_owner_name"):
            user_session["appointment"]["phone"] = from_number
            user_session["appointment"]["id"] = random.randint(1, 99999)
        elif not form.get("asked_pet_name"):
            user_session["appointment"]["owner_name"] = information
        elif not form.get("asked_document_id"):
            user_session["appointment"]["pet_name"] = information
        elif not form.get("asked_date"):
            user_session["appointment"]["document_id"] = information
        elif not form.get("asked_time"):
            user_session["appointment"]["date"] = information
        elif not form.get("asked_type"):
            user_session["appointment"]["appointment_time"] = information
        else:
            user_session["appointment"]["type"] = type_mapping[information]
            user_session["appointment"]["state"] = PENDING

    def validate_input(self, input: str, user_session) -> bool:
        """
        Validate if input is valid
        """
        if not user_session["asked_owner_name"]:
            return True
        elif not user_session["asked_pet_name"]:
            return True
        elif not user_session["asked_document_id"]:
            return True
        elif not user_session["asked_date"]:
            return input.isnumeric()
        elif not user_session["asked_time"]:
            return self._validate_date(input)
        elif not user_session["asked_type"]:
            return True
        else:
            if user_session["asked_time"]:
                return self._validate_time(input)
            return True

    def _validate_date(self, date: str) -> bool:
        """
        Validate if date is valid and not earlier than the current date.
        """
        try:
            # Parse the input date
            input_date = datetime.datetime.strptime(date, '%d/%m/%Y')

            # Get the current date
            current_date = datetime.datetime.now()

            # Compare the input date with the current date
            if input_date >= current_date:
                return True
            else:
                return False
        except ValueError:
            return False
        
    def _validate_time(self, time: str) -> bool:
        """
        Validate if time is valid
        """
        try:
            datetime.datetime.strptime(time, '%H:%M')
            return True
        except ValueError:
            return False

    def get_state_message(self, user_session: dict) -> str:
        """
        Get the valid message to ask user based on information missing
        """
        if not user_session.get("asked_owner_name"):
            user_session["asked_owner_name"] = True
            return self.commerce.messages.user_name_msg
        elif not user_session.get("asked_pet_name"):
            user_session["asked_pet_name"] = True
            return self.commerce.messages.pet_name_msg
        elif not user_session.get("asked_document_id"):
            user_session["asked_document_id"] = True
            return self.commerce.messages.document_id_msg
        elif not user_session.get("asked_date"):
            user_session["asked_date"] = True
            return self.commerce.messages.appointment_date_msg
        elif not user_session.get("asked_time"):
            user_session["asked_time"] = True
            return self.commerce.messages.appointment_time_msg
        elif not user_session.get("asked_type"):
            user_session["asked_type"] = True
            return self.commerce.messages.appointment_type_msg
        return ''  # Empty means all values are completed

    def reset_form_state(self, user_session: dict):
        """
        Reset form state to validate new appointments
        """
        form: dict = user_session["appointment_questions"]  # only the questions dict
        form["asked_owner_name"] = False
        form["asked_pet_name"] = False
        form["asked_document_id"] = False
        form["asked_date"] = False
        form["asked_time"] = False
        form["asked_type"] = False
        user_session["is_handle_new_appointment"] = False

    def to_dict(self) -> dict:
        """
        Convert AppointmentForm to dict
        """
        return {
            "appointment_questions": {
                'asked_owner_name': self.asked_owner_name,
                'asked_pet_name': self.asked_pet_name,
                'asked_document_id': self.asked_document_id,
                'asked_date': self.asked_date,
                'asked_type': self.asked_type,
                'asked_time': self.asked_time,
            },
            'is_handle_new_appointment': self.is_handle_new_appointment,
            'appointment': self.appointment.to_dict(),
            'commerce': self.commerce.to_dict()
        }
