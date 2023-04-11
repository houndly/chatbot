from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
from flask_ngrok import run_with_ngrok


app = Flask(__name__)
run_with_ngrok(app)


@app.route("/sms", methods=["POST"])
def reply():
    incoming_msg = request.form.get("Body").lower()
    response = MessagingResponse()
    message = response.message()
    responded = False
    words = incoming_msg.split("")
    if "hola" in words:
        message.body("Hola, soy un bot de prueba")
        responded = True

    if not responded:
        message.body("No se que decir")

    return str(response)


if __name__ == "__main__":
    app.run()
