"""
Send WhatsApp message using pywhatkit (system-based).
"""

import pywhatkit as kit
import datetime

def send_whatsapp_pywhatkit(phone_number: str, message: str) -> str:
    try:
        now = datetime.datetime.now()
        hour = now.hour
        minute = now.minute + 2

        kit.sendwhatmsg(phone_number, message, hour, minute, wait_time=10)
        return "Message scheduled using pywhatkit."
    except Exception as e:
        return f"Error sending message with pywhatkit: {str(e)}"