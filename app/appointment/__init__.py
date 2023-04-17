from app.common.sheets import getConnection as sheets

def register_appointment() -> bool:
	"""
 	Registers an appointment with the veterinarian
  """
	# Set row values to insert
	new_row = [] # TODO: ADD Class to handle values to insert into row
	registration = sheets.insert_data(new_row) # Set sheet connection
	return registration # New appointment register successfully