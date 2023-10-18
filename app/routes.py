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
from app.appointment.main import get_all_appointments, get_day_appointments, get_week_appointments, create_new_appointment
from flask_cors import CORS  # Import the CORS module

# Initialize CORS with default options
CORS(app)

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


@app.route("/api/appointments", methods=["GET"])
def appointments():
    appointments_data = get_all_appointments()
    return jsonify(appointments_data)


@app.route("/api/appointments/day", methods=["GET"])
def appointmentsForDay():
    appointments_data = get_day_appointments()
    return jsonify(appointments_data)


@app.route("/api/appointments/week", methods=["GET"])
def appointmentsForWeek():
    appointments_data = get_week_appointments()
    return jsonify(appointments_data)

@app.route("/api/appointment", methods=["POST"])
def CreateAppointment():
    try:
        appointment_data = request.get_json()
        created_appointment = create_new_appointment(appointment_data)  
        return jsonify(created_appointment), 201  # 201 significa 'Creado' en el estándar HTTP
    except Exception as e:
        return jsonify({"error": str(e)}), 400  # 400 significa 'Solicitud incorrecta' en el estándar HTTP