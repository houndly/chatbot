from typing import List
from app.commerce.commerce_messages_model import CommerceMessagesModel
from app.commerce.commerce_model import CommerceModel
from app.common.constants import DEFAULT_COMMERCE_DATA
from app.common.remote import get_remote_data

# List of commerce information saved each time is consulting
# This is to avoid requests from remote services to get the same data
commerce_data_models: List[CommerceModel] = []


def get_commerce_data(commerce_id: str) -> CommerceModel:
    """
    Get the message data by commerce used on chatbot based on commerce
    Information like commerce data and messages to show on each chatbot

    Parameters:
        commerce_id: Represents the ID of the commerce user is chatting with (phone number from Twilio),
                        This value is going to represent if it is necessary to get a json file from remote source
                        or with the saved data filles is enough to response user requests
    """
    commerce_exists = False
    for model in commerce_data_models:
        if model.commerce_id == commerce_id:
            commerce_exists = True

    if commerce_exists:
        return commerce_data_models[commerce_id]
    else:
        # TODO: ADD url to json file
        data = get_remote_data("", DEFAULT_COMMERCE_DATA)
        commerce = CommerceModel(
            commerce_id=data['commerce_id'],
            name=data['name'], messages=CommerceMessagesModel(**data['messages']))
        # Save new model into list of models
        commerce_data_models.append(commerce)
        return commerce
