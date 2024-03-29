"""
Entity to handle appointments information

Properties to create or update an appointment
"""
from datetime import datetime
from dataclasses import dataclass


@dataclass
class AppointmentModel:
    """
    Appointment entity class
    """
    id: str = None
    owner_name: str = None
    pet_name: str = None
    phone: int = None
    document_id: int = None
    date: datetime = None
    appointment_time: str = None
    state: str = None
    type: str = None

    def get_data_to_row(self) -> list:
        """
        Get data to be insert inside the sheet row
        """

        return [self.id, self.owner_name, self.pet_name, self.phone, self.document_id, self.date, self.appointment_time, self.type, self.state ]

    def get_appointment_info(self) -> str:
        state_emoji = ""
        if self.state == "Confirmada":
            state_emoji = "✅"  # Emoji para estado confirmado
        elif self.state == "Pendiente":
            state_emoji = "⏳"  # Emoji para estado pendiente
        elif self.state == "Cancelada":
            state_emoji = "❌"  # Emoji para estado eliminado

        return f"💳 ID: {self.id} \n🐶🐱 Nombre: {self.pet_name} \n🗓️ Fecha: {self.date} \n🕕 Hora: {self.appointment_time} \n👀 Tipo: {self.type} \n{state_emoji} Estado: {self.state} "

    def to_dict(self) -> dict:
        return {
            "owner_name": self.owner_name,
            "pet_name": self.pet_name,
            "phone": self.phone,
            "document_id": self.document_id,
            "date": self.date,
            "appointment_time": self.appointment_time,
            "state": self.state,
            "type": self.type
        }
