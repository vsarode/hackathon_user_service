from user_service.db.user_models.models import User
from twilio.rest import Client

def OTPvalidation(user):
      try:
          phone=user.phone
          a="+91"
          a=str(a)+str(phone)

          account_sid = "AC4236a90255257d6356d8e387d87915e8"
          auth_token = "0b2c5d372e262ee52f448671bad3ad4e"

          client = Client(account_sid, auth_token)

          client.api.account.messages.create(to=a,from_="+19388008284",body="shubham")

      except Exception as e:
          print e
          return None


