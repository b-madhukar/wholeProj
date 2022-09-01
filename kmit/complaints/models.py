from django.db import models
from django import forms
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save
from client.models import Profile
from django.core.validators import RegexValidator
from datetime import datetime

# Create your models here.
class Complaint(models.Model):
    STATUS =((1,'Solved'),(2, 'InProgress'),(3,'Pending'))
    TYPE=(('ITPerson',"ITPerson"),('Electrician',"Electrician"),('Plumber',"Plumber"),('Gardener',"Gardener"),('Other',"Other"))
    Subject=models.CharField(max_length=200,blank=False,null=True)
    user_name=models.ForeignKey(Profile, on_delete=models.CASCADE,default=None)
    contactnumber=models.CharField(max_length=200,blank=False,null=True)
    Type_of_complaint=models.CharField(choices=TYPE,null=True,max_length=200)
    Description=models.TextField(max_length=4000,blank=False,null=True)
    Time = models.DateField(auto_now=True)
    status=models.IntegerField(choices=STATUS,default=3)
    def __str__(self):
        return self.user_name
    