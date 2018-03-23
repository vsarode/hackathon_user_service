# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BillingEntry',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('month', models.DateTimeField(default=datetime.datetime(2018, 3, 23, 13, 15, 39, 590391))),
                ('billing_units', models.IntegerField()),
                ('bill_amount', models.IntegerField()),
                ('is_paid', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Complaint',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(default=None, max_length=256)),
                ('complaint_text', models.CharField(max_length=1024)),
                ('status', models.CharField(default=None, max_length=124, choices=[(b'Viewed', b'Viewed'), (b'Processing', b'Processing'), (b'Done', b'Done')])),
            ],
        ),
        migrations.CreateModel(
            name='Connection',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('customer_id', models.CharField(max_length=256, null=True)),
                ('survey_number', models.CharField(max_length=254)),
                ('society_name', models.CharField(max_length=256)),
                ('line_no1', models.CharField(max_length=256, null=True)),
                ('line_no2', models.CharField(max_length=256, null=True)),
                ('village', models.CharField(max_length=256, null=True)),
                ('taluka', models.CharField(max_length=256, null=True)),
                ('district', models.CharField(max_length=254, null=True)),
                ('state', models.CharField(max_length=256, null=True)),
                ('pincode', models.IntegerField()),
                ('supply_type', models.CharField(default=None, max_length=124, choices=[(b'Single_phase', b'Single_phase'), (b'Three_phase', b'Three_phase'), (b'HT_supply', b'HT_supply')])),
                ('consumer_type', models.CharField(default=None, max_length=124, choices=[(b'LT', b'LT'), (b'HT', b'HT'), (b'EHV', b'EHV')])),
                ('created_on', models.DateTimeField(default=datetime.datetime(2018, 3, 23, 13, 15, 39, 587284))),
                ('is_valid', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='LoginEntry',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('login_time', models.DateTimeField(default=datetime.datetime(2018, 3, 23, 13, 15, 39, 588588))),
                ('auth_token', models.CharField(default=b'93dad43d-daa4-43e2-86ff-ff2fcbb324dd', max_length=512)),
                ('is_active', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='OTP',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('otp', models.IntegerField()),
                ('is_valid', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('question_string', models.CharField(max_length=256)),
                ('question_time', models.DateTimeField(default=datetime.datetime(2018, 3, 23, 13, 15, 39, 589918))),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('username', models.CharField(max_length=254, serialize=False, primary_key=True)),
                ('password', models.CharField(max_length=256)),
                ('phone', models.CharField(max_length=20, null=True)),
                ('is_confirmed', models.BooleanField(default=False)),
                ('connection', models.ForeignKey(to='user_models.Connection')),
            ],
        ),
        migrations.AddField(
            model_name='question',
            name='user',
            field=models.ForeignKey(to='user_models.User'),
        ),
        migrations.AddField(
            model_name='otp',
            name='user',
            field=models.ForeignKey(to='user_models.User'),
        ),
        migrations.AddField(
            model_name='loginentry',
            name='user',
            field=models.ForeignKey(to='user_models.User'),
        ),
        migrations.AddField(
            model_name='complaint',
            name='user',
            field=models.ForeignKey(to='user_models.User'),
        ),
        migrations.AddField(
            model_name='billingentry',
            name='user',
            field=models.ForeignKey(to='user_models.User'),
        ),
    ]
