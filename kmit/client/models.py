from django.db import models
from django import forms
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save

from django.core.validators import RegexValidator
from datetime import datetime
from django.contrib.auth.hashers import make_password

# Create your models here.
class Profile(models.Model):
    user_name=models.CharField(max_length=120)
    first_name=models.CharField(max_length=120)
    last_name=models.CharField(max_length=120)
    phone_regex =RegexValidator(regex=r'^\d{10,10}$', message="Phone number must be entered in the format:Up to 10 digits allowed.")
    contactnumber = models.CharField(validators=[phone_regex], max_length=10, blank=True) 
    email_id = models.EmailField(max_length = 254,default='')
    password = models.CharField(max_length=30)
    def __str__(self):
        return self.user_name
    