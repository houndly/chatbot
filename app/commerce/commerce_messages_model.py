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
