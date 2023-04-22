from dataclasses import dataclass

from app.commerce.commerce_messages_model import CommerceMessagesModel


@dataclass
class CommerceModel:
    """
    Information about commerce and data to show to user

    Parameters
        commerce_id: Represent the identifier of the Commerce
        name: Name of the commerce
        message: Messages commerce want to display into the chatbot
    """
    commerce_id: str = None
    name: str = None
    messages: CommerceMessagesModel = None
