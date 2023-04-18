"""
Module to locate constant values in the APP
"""
import os
from enum import Enum

# Path to google sheets credentials using os module
GOOGLE_SHEETS = os.path.join(os.path.dirname(__file__), "credentials.json")

# Options from menu user can select
CHECK_APPOINTMENTS = '1'
NEW_APPOINTMENT = '2'

# Columns ID in array rows inside appointment google Sheets
OWNER_NAME_COLUMN_ORDER = 1
PET_NAME_COLUMN_ORDER = 2
PHONE_COLUMN_ORDER = 3
DOCUMENT_COLUMN_ORDER = 4
DATE_COLUMN_ORDER = 4
TIME_COLUMN_ORDER = 5
STATE_COLUMN_ORDER = 6
