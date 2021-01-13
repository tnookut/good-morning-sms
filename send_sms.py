from twilio.rest import Client
import schedule
import time
from credentials import account_sid, auth_token, twilio_num, mobile_num

# The message to be sent.
quote = 'Good Morning! :)'

# Send SMS text.
def send_message():

    # Authenticate client
    client = Client(account_sid, auth_token)

    # Send message from twilio phone number to mobile phone number.
    message = client.messages.create(
        to=mobile_num, 
        from_=twilio_num,
        body=quote)
    

# Schedule a time to send the message
schedule.every().day.at("08:00").do(send_message)

while True:
    schedule.run_pending()
    time.sleep(2)

