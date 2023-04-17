"""
	Module to locate constant values in the APP
"""
import os
from enum import Enum
# Path to google sheets credentials using os module
GOOGLE_SHEETS = os.path.join(os.path.dirname(__file__), "credentials.json")

class MenuOptions(Enum):
  """
  Enum with menu options can user select
  """
  CHECK_APPOINTMENTS: 1
  NEW_APPOINTMENT: 2