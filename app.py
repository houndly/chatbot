from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse

app = Flask(__name__)


@app.route("/sms", methods=["POST"])
def reply():
    incoming_msg = request.form.get("Body").lower()
    response = MessagingResponse()
    words = incoming_msg.split(" ")
    if words:
        resp_txt = "Hello World"
        response.message(resp_txt)

    return str(response)

@app.route("/status", methods=["GET"])
def status():
    return "OK"


if __name__ == "__main__":
    app.run()
