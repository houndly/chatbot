"""
Entity to handle appointments information

Properties to create or update an appointment
"""
from app.appointment.constants import AppointmentStateType
from datetime import datetime


class Appointment:
	"""
	Appointment entity class
	"""
	def __init__(self, owner_name: str, pet_name: str, phone: int, document_id: int, date: datetime, appointment_time: str, state: AppointmentStateType):
		self._owner_name = owner_name
		self._pet_name = pet_name
		self._phone = phone
		self._document_id = document_id
		self._date = date
		self._appointment_time = appointment_time
		self._state = state

	@property
	def owner_name(self) -> str:
			return self._owner_name

	@owner_name.setter
	def owner_name(self, value: str):
		self._owner_name = value

	@property
	def pet_name(self) -> str:
		return self._pet_name

	@pet_name.setter
	def pet_name(self, value: str):
		self._pet_name = value

	@property
	def phone(self) -> int:
		return self._phone

	@phone.setter
	def phone(self, value: int):
		self._phone = value

	@property
	def document_id(self) -> int:
		return self._document_id

	@document_id.setter
	def document_id(self, value: int):
		self._document_id = value

	@property
	def date(self) -> datetime:
		return self._date

	@date.setter
	def date(self, value: datetime):
		self._date = value

	@property
	def appointment_time(self) -> str:
		return self._appointment_time

	@appointment_time.setter
	def appointment_time(self, value: str):
		self._appointment_time = value

	@property
	def date_state(self) -> AppointmentStateType:
		return self._state

	@date_state.setter
	def date_state(self, value: AppointmentStateType):
		self._state = value

	def get_data_to_row(self) -> list:
		"""
		Get data to be insert inside the sheet row
		"""
		return [self._owner_name, self._pet_name, self._phone, self._document_id, self._date, self._appointment_time, self._state]