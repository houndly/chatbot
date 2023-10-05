# Appointment state possible values
PENDING = 'Pendiente'
CANCEL = 'Cancelada'
DONE = 'Realizada'
BREACH = 'Incumplimiento'

# ID of the sheet to handle CRUD of appointments
# APPOINTMENTS_SHEET_ID = '13IogyxGONgFFCOlz5U2z1aLHz6BfSXKddrIoboqB6H4'
APPOINTMENTS_SHEET_ID = '1CC9G-tmXDXmaoc-ceSHvb8gBLb7K_v9wiuWFEkeEfk8'
ID_SCHEDULES_SHEET = "Horarios"
ID_APPOINTMENTS_SHEET = "Citas_agendadas"

TYPE_MAPPING = {
    "1": "Vacunación 🐾",
    "2": "Desparasitación 🦠",
    "3": "Consulta médica 🩺",
    "4": "Ecografía 📡",
    "5": "Radiografía 📷",
    "6": "Baño y peluquería ✂️",
    "7": "Exámenes de laboratorio 🧪",
    "8": "Profilaxis 🦷"
}

TIME_MAPPING_WEEKEND = {
    "1": "9:00 AM -> 10:00 AM ",
    "2": "10:00 AM -> 11:00 AM ",
    "3": "11:00 AM -> 12:00 AM ",
    "4": "12:00 PM -> 1:00 PM ",
    "5": "1:00 PM -> 2:00 PM ",
    "6": "2:00 PM -> 3:00 PM ",
}
TIME_MAPPING_WEEKLY = {
    "1": "9:00 AM -> 10:00 AM ",
    "2": "10:00 AM -> 11:00 AM ",
    "3": "11:00 AM -> 12:00 AM ",
    "4": "12:00 PM -> 1:00 PM ",
    "5": "1:00 PM -> 2:00 PM ",
    "6": "2:00 PM -> 3:00 PM ",
    "7": "3:00 PM -> 4:00 PM ",
    "8": "4:00 PM -> 5:00 PM ",
    "9": "5:00 PM -> 6:00 PM ",
}
