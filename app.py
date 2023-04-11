from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse


app = Flask(__name__)


@app.route("/sms", methods=["POST"])
def reply():
    incoming_msg = request.form.get("Body").lower()
    response = MessagingResponse()
    message = response.message()


if __name__ == "__main__":
    app.run(debug=True)
