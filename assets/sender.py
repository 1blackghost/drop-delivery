from twilio.rest import Client


def send_whatsapp_message(to_number, message_body):
    # Replace these with your actual Twilio credentials
    account_sid = 'AC356901ac8afcb9ffe13bfd6fcfd3e4fc'
    auth_token = '3d447ce1d48b02638eb7b7444266af4f'

    client = Client(account_sid, auth_token)
    print(message_body)
    try:
        message = client.messages.create(
            from_='whatsapp:+14155238886',  # Replace with your Twilio WhatsApp number
            body=message_body,
            to=f'whatsapp:{to_number}'
        )

        print(f"Message sent successfully to {to_number}. SID: {message.sid}")

    except Exception as e:
        print(f"Error sending message to {to_number}: {str(e)}")

'''
# Example Usage:
to_phone_number = '918547413213'  # Replace with the recipient's phone number
message_content = 'Hello! This is a test message.'  # Replace with your actual message
send_whatsapp_message(to_phone_number, message_content)
'''