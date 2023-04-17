"""
Entity to handle appointments information

Properties to create or update an appointment
"""
from app.appointment.constants import AppointmentStateType
from datetime import datetime
from dataclasses import dataclass

@dataclass
class Appointment:
	"""
	Appointment entity class
	"""
	owner_name: str
	pet_name: str
	phone: int
	document_id: int
	date: datetime
	appointment_time: str
	state: AppointmentStateType

	def get_data_to_row(self) -> list:
		"""
		Get data to be insert inside the sheet row
		"""
		return [self.owner_name, self.pet_name, self.phone, self.document_id, self.date, self.appointment_time, self.state]

	def get_appointment_info(self) -> str:
		return f"Mascota: {self.pet_name} \nFecha: {self.date} \nHora: {self.appointment_time}"