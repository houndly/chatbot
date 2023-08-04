from dataclasses import dataclass


@dataclass
class CommerceMessagesModel:
    """
    Model with message to show for each commerce

    Message are those user is going to see on each flow using the bot
    """
    # Welcome
    initial_msg: str = None
    # General error
    error_msg: str = None
    # Error when user input is not valid
    format_error_msg: str = None
    # Goodbye message (when user don't want to continue with the chat)
    good_bye_msg: str = None
    # User select new appointment option
    new_appointment_msg: str = None
    # Previous to show list of current appointments for user
    current_appointments_msg: str = None
    # Appointment added successfully
    appointment_added_msg: str = None
    # Ask user if they want to continue with the chat
    continue_chat_msg: str = None
    # Adding appointment - User name
    user_name_msg: str = None
    # Adding appointment - User pet's name
    pet_name_msg: str = None
    # Adding appointment - Document id number
    document_id_msg: str = None
    # Adding appointment - Appointment date
    appointment_date_msg: str = None
    # Adding appointment - Appointment time
    appointment_time_msg: str = None
    
    appointment_pending_msg: str = None

    appointment_type_msg: str = None
    appointment_delete_msg: str = None
    appointment_delete_success_msg: str = None
    appointment_delete_err_msg: str = None

    def to_dict(self):
        """
        Convert CommerceMessagesModel to dict
        """
        return {
            "initial_msg": self.initial_msg,
            "error_msg": self.error_msg,
            "good_bye_msg": self.good_bye_msg,
            "new_appointment_msg": self.new_appointment_msg,
            "current_appointments_msg": self.current_appointments_msg,
            "appointment_added_msg": self.appointment_added_msg,
            "continue_chat_msg": self.continue_chat_msg,
            "user_name_msg": self.user_name_msg,
            "pet_name_msg": self.pet_name_msg,
            "document_id_msg": self.document_id_msg,
            "appointment_date_msg": self.appointment_date_msg,
            "appointment_time_msg": self.appointment_time_msg,
            "appointment_pending_msg": self.appointment_pending_msg,
            "appointment_type_msg": self.appointment_type_msg,
            "appointment_delete_msg": self.appointment_delete_msg,
            "appointment_delete_success_msg": self.appointment_delete_success_msg,
            "appointment_delete_err_msg": self.appointment_delete_err_msg
        }
