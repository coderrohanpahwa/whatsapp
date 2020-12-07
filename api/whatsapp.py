from twilio.rest import Client

# client credentials are read from TWILIO_ACCOUNT_SID and AUTH_TOKEN
client = Client('ACc2a7e10a8a382fc0595bd51a422de800','6daf149c93a7b1715bcd2e0b1e250f9a')

# this is the Twilio sandbox testing number
# from_whatsapp_number='whatsapp:+91155238886'
from_whatsapp_number='whatsapp:+14155238886'
# replace this number with your own WhatsApp Messaging number
to_whatsapp_number='whatsapp:+918221988235'

message=client.messages.create(body='Hello Rohan Pahwa',
                       from_=from_whatsapp_number,
                       to=to_whatsapp_number)
print(message)
print(message.sid)
