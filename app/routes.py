"""
	This module defines the routes for the Flask app.

	Routes:
		/: Returns the data based on interaction with the Bot.
		/status: Returns the status of the server.
"""

import pytz
from datetime import datetime
from flask import request, jsonify
from app import app
from app.common.menu import handle_menu


@app.route('/bot', methods=["POST"])
def bot():
    """
            Handle interaction with Twilio and Chatbot based on user interaction and
            numbers selected on menu map

            Returns:
                    JSON response to show users on WhatsApp
    """
    incoming_msg = request.form
    return handle_menu(incoming_msg)


@app.route("/status", methods=["GET"])
def status():
    """
            Show status of the server

            Returns:
                    status: status server
    """
    colombia_tz = pytz.timezone('America/Bogota')
    return jsonify({'status': f'OK - {datetime.now(colombia_tz).strftime("%a %d|%m|%Y %H:%M:%S")}'}), 200
