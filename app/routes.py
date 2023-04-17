"""
	This module defines the routes for the Flask app.

	Routes:
		/: Returns the data based on interaction with the Bot.
		/status: Returns the status of the server.
"""

from flask import request, jsonify
from twilio.twiml.messaging_response import MessagingResponse
from app.common.sheets import get_appointments
from app import app

# Define the app routes here

@app.route('/bot', methods=["POST"])
def bot():
	"""
		Handle interaction with Twilio and Chatbot based on user interaction and
		numbers selected on menu map

		Returns:
			JSON response to show users on WhatsApp
	"""
	incoming_msg = request.form.get('Body').lower()
	response = MessagingResponse()
	if incoming_msg not in ["1", "2"]:
		response.message("Hola, gracias por escribirnos. Empecemos eligiendo una opción del menú: \n 1. Consultar citas \n 2. Agendar cita")
		return str(response)
	if incoming_msg == "1":
		appointments = get_appointments("13IogyxGONgFFCOlz5U2z1aLHz6BfSXKddrIoboqB6H4")
		response.message("Estas son tus citas: ")
		for appointment in appointments:
			response.message("Mascota: " + appointment["Mascota"] + "\nFecha: " + appointment["Fecha"] + "\nHora: " + appointment["Hora"])
		return str(response)
	if incoming_msg == "2":
		pass

@app.route("/status", methods=["GET"])
def status():
	"""
		Show status of the server

		Returns:
			status: status server
	"""
	return jsonify({'status': 'OK'}), 200
