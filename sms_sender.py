"""
sms_sender.py

Send SMS messages using Twilio.
"""

import os
from dotenv import load_dotenv
from twilio.rest import Client

load_dotenv()

def send_sms(to_number: str, message: str) -> str:
    try:
        account_sid = os.getenv("your_account_sid")
        auth_token = os.getenv("your_auth_token")
        from_number = os.getenv("+your_twilio_number")

        if not all([account_sid, auth_token, from_number]):
            return "Error: Twilio credentials missing in environment."

        client = Client(account_sid, auth_token)
        sms = client.messages.create(
            to=to_number,
            from_=from_number,
            body=message
        )

        return f"SMS sent successfully. SID: {sms.sid}"
    except Exception as e:
        return f"Failed to send SMS: {str(e)}"