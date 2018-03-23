import uuid
from datetime import datetime

from django.db import models


class Connection(models.Model):
    CONSUMER_TYPE = (("LT", "LT"),
                     ("HT", "HT"),
                     ("EHV", "EHV"))
    SUPPLY_TYPE = (("Single_phase", "Single_phase"),
                   ("Three_phase", "Three_phase"),
                   ("HT_supply", "HT_supply"))
    customer_id = models.CharField(max_length=256, null=True)
    survey_number = models.CharField(max_length=254)
    society_name = models.CharField(max_length=256)
    line_no1 = models.CharField(max_length=256, null=True)
    line_no2 = models.CharField(max_length=256, null=True)
    village = models.CharField(max_length=256, null=True)
    taluka = models.CharField(max_length=256, null=True)
    district = models.CharField(max_length=254, null=True)
    state = models.CharField(max_length=256, null=True)
    pincode = models.IntegerField()
    supply_type = models.CharField(max_length=124, choices=SUPPLY_TYPE,
                                   default=None)
    consumer_type = models.CharField(max_length=124, choices=CONSUMER_TYPE,
                                     default=None)
    created_on = models.DateTimeField(default=datetime.now())
    is_valid = models.BooleanField(default=False)


class User(models.Model):
    username = models.CharField(max_length=254, primary_key=True)
    password = models.CharField(max_length=256)
    phone = models.CharField(max_length=20, null=True)
    is_confirmed = models.BooleanField(default=False)
    connection = models.ForeignKey(Connection)


class LoginEntry(models.Model):
    user = models.ForeignKey(User)
    login_time = models.DateTimeField(default=datetime.now())
    auth_token = models.CharField(max_length=512, default=str(uuid.uuid4()))
    is_active = models.BooleanField(default=True)


class OTP(models.Model):
    user = models.ForeignKey(User)
    otp = models.IntegerField()
    is_valid = models.BooleanField(default=True)


class Question(models.Model):
    user = models.ForeignKey(User)
    question_string = models.CharField(max_length=256)
    question_time = models.DateTimeField(default=datetime.now())


# class Answer(models.Model):
#     question=models.ForeignKey()
#     answer_string = models.CharField(max_length=256)
#     answer_time = models.DateTimeField(default=datetime.now())

class BillingEntry(models.Model):
    user = models.ForeignKey(User)
    month = models.DateTimeField(default=datetime.now())
    billing_units = models.IntegerField()
    bill_amount = models.IntegerField()
    is_paid = models.BooleanField(default=False)


class Complaint(models.Model):
    STATUS = (("Viewed", "Viewed"),
              ("Processing", "Processing"),
              ("Done", "Done"))
    user = models.ForeignKey(User)
    name = models.CharField(max_length=256, default=None)
    complaint_text = models.CharField(max_length=1024)
    status = models.CharField(max_length=124, choices=STATUS, default=None)
