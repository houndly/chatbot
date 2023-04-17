"""
	This module defines the routes for the Flask app.

	Routes:
		/: Returns the data based on interaction with the Bot.
		/status: Returns the status of the server.
"""

from flask import request, jsonify
from app.common.menu import handle_menu
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
	return handle_menu(incoming_msg)

@app.route("/status", methods=["GET"])
def status():
	"""
		Show status of the server

		Returns:
			status: status server
	"""
	return jsonify({'status': 'OK UPDATE 17/04/2023'}), 200
