import os
import smtpd
import asyncore
import re
from twilio.rest import Client

# CONFIGURATION (Use Environment Variables for security)
TWILIO_ACCOUNT_SID = os.getenv('TWILIO_SID', 'your_sid_here')
TWILIO_AUTH_TOKEN = os.getenv('TWILIO_TOKEN', 'your_token_here')
TWILIO_FROM_NUMBER = os.getenv('TWILIO_NUM', '+15550000000')

class SMSServer(smtpd.SMTPServer):
    def process_message(self, peer, mailfrom, rcpttos, data, **kwargs):
        """
        Intercepts email from GoPhish and converts it to SMS.
        """
        print(f"[*] Intercepted message destined for: {rcpttos}")
        
        # decoding data
        message_body = data.decode('utf-8')
        
        # Extract the link/message content (Simple regex to find the URL)
        # In a real campaign, you'd parse the MIME parts.
        url_match = re.search(r'(https?://[^\s]+)', message_body)
        
        if url_match:
            clean_message = f"Twilio Security Alert: Unusual activity detected. Verify identity: {url_match.group(0)}"
            self.send_sms(rcpttos, clean_message)
        else:
            print("[!] No URL found in message body.")

    def send_sms(self, to_email, body):
        """
        Sends the actual SMS via Twilio API.
        Assumes the 'email' in GoPhish is actually a phone number (e.g. +1555999@sms.local)
        """
        try:
            # Extract phone number from the "email" address
            phone_number = to_email.split('@')
            
            client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)
            message = client.messages.create(
                body=body,
                from_=TWILIO_FROM_NUMBER,
                to=phone_number
            )
            print(f"[+] SMS Sent to {phone_number}: SID {message.sid}")
        except Exception as e:
            print(f"[-] Failed to send SMS: {e}")

if __name__ == '__main__':
    print("[*] Starting SMS Middleware on port 1025...")
    # GoPhish should be configured to send email to localhost:1025
    server = SMSServer(('0.0.0.0', 1025), None)
    try:
        asyncore.loop()
    except KeyboardInterrupt:
        print("Stopping server.")
