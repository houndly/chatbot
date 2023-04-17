from enum import Enum

class AppointmentStateType(Enum):
  """
  Enum with valid states for appointment

  This information is based on Sheets states values
  """
  PENDING: "Pendiente"
  CANCEL: "Cancelada"
  DONE: "Realizada"
  BREACH: "Incumplimiento"