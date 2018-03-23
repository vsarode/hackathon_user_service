from twilio.rest import Client

account_sid = 'AC4236a90255257d6356d8e387d87915e8'  # Found on Twilio Console Dashboard
auth_token = '0b2c5d372e262ee52f448671bad3ad4e'  # Found on Twilio Console Dashboard

sender = '+919762778870'  # Phone number you used to verify your Twilio account
receiver = '+919637552245'  # Phone number given to you by Twilio


def send_sms(sender, receiver):
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        to=receiver,
        from_=sender,
        body="hi i am shubham")
    print "Done!!", message


if __name__ == "__main__":
    send_sms(sender, receiver)
