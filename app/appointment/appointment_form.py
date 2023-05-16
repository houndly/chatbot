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
        form: dict = user_session["appointment_questions"] # only the questions dict

        if not form.get("asked_owner_name"):  # self.asked_owner_name:
            # self.appointment.phone = from_number
            user_session["appointment"]["phone"] = from_number
        elif not form.get("asked_pet_name"):  # self.asked_pet_name:
            # self.appointment.owner_name = information
            user_session["appointment"]["owner_name"] = information
        # self.asked_document_id:
        elif not form.get("asked_document_id"):
            # self.appointment.pet_name = information
            user_session["appointment"]["pet_name"] = information
        elif not form.get("asked_date"):  # self.asked_date:
            # self.appointment.document_id = information
            user_session["appointment"]["document_id"] = information
        elif not form.get("asked_time"):  # self.asked_time:
            # self.appointment.date = information
            user_session["appointment"]["date"] = information
        else:
            user_session["appointment"]["appointment_time"] = information
            # self.appointment.appointment_time = information
            # New appointments always are PENDING by default
            user_session["appointment"]["state"] = PENDING
            # self.appointment.state = PENDING

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
        else:
            if user_session["asked_time"]:
                return self._validate_time(input)
            return True

    def _validate_date(self, date: str) -> bool:
        """
        Validate if date is valid
        """
        try:
            datetime.datetime.strptime(date, '%d/%m/%Y')
            return True
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

        # if not self.asked_owner_name:
        #     self.asked_owner_name = True
        #     return self.commerce.messages.user_name_msg
        # elif not self.asked_pet_name:
        #     self.asked_pet_name = True
        #     return self.commerce.messages.pet_name_msg
        # elif not self.asked_document_id:
        #     self.asked_document_id = True
        #     return self.commerce.messages.document_id_msg
        # elif not self.asked_date:
        #     self.asked_date = True
        #     return self.commerce.messages.appointment_date_msg
        # elif not self.asked_time:
        #     self.asked_time = True
        #     return self.commerce.messages.appointment_time_msg
        # return ''  # Empty means all values are completed
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
        return ''  # Empty means all values are completed

    def reset_form_state(self, user_session: dict):
        """
        Reset form state to validate new appointments
        """
        # self.asked_owner_name = False
        # self.asked_pet_name = False
        # self.asked_document_id = False
        # self.asked_date = False
        # self.asked_time = False
        # self.is_handle_new_appointment = False
        form: dict = user_session["appointment_questions"] # only the questions dict
        form["asked_owner_name"] = False
        form["asked_pet_name"] = False
        form["asked_document_id"] = False
        form["asked_date"] = False
        form["asked_time"] = False
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
                'asked_time': self.asked_time, 
            },
            'is_handle_new_appointment': self.is_handle_new_appointment,
            'appointment': self.appointment.to_dict(),
            'commerce': self.commerce.to_dict()
        }
