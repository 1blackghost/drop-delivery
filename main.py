from flask import Flask, request
from assets import sender,process_request
from twilio.twiml.messaging_response import MessagingResponse #not used converts to xml
from twilio.rest import Client

app = Flask(__name__)


@app.route('/', methods=["POST","GET"])
def respond_to_whatsapp():

    incoming_message = request.values.get('Body', '').lower()
    user_phone = request.values.get('From')
    print(f"Incoming message from {user_phone}: {incoming_message}")
    user_phone=user_phone.split("+")[1]
    print(user_phone)
    response=(process_request.process(str(incoming_message),str(user_phone)))
    sender.send_whatsapp_message(user_phone,response)




if __name__ == '__main__':
    app.run(debug=True)
