from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
from flask_ngrok import run_with_ngrok


app = Flask(__name__)
run_with_ngrok(app)


@app.route("/sms", methods=["POST"])
def reply():
    incoming_msg = request.form.get("Body").lower()
    response = MessagingResponse()
    words = incoming_msg.split(" ")
    if words:
        resp_txt = "Hello World"
        response.message(resp_txt)

    return str(response)


if __name__ == "__main__":
    app.run()
