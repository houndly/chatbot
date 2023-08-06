"""
Entity to handle appointments information

Properties to create or update an appointment
"""
from datetime import datetime
from dataclasses import dataclass


@dataclass
class ScheduleModel:
    """
    Appointment entity class
    """
    id: str = None
    date: datetime = None
    time_init: str = None
    time_end: str = None

    def get_data_to_row(self) -> list:
        """
        Get data to be insert inside the sheet row
        """
        return [self.id, self.date, self.time_init, self.time_end]
