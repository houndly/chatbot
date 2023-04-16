"""
	Module to locate constant values in the APP
"""
from enum import Enum

class CredentialsFiles(Enum):
  """
  Enum with credentials files location
  """
  GOOGLE_SHEETS = '/google_sheets_credentials.json'

class MenuOptions(Enum):
  """
  Enum with menu options can user select
  """
  CHECK_APPOINTMENTS: 1
  NEW_APPOINTMENT: 2