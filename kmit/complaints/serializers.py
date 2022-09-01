from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Complaint
from .models import Profile
from rest_framework.response import Response
from rest_framework import status
from rest_framework.validators import UniqueValidator
from django.contrib.auth.password_validation import validate_password

#Serializer to Get User Details using Django Token Authentication
class ComplaintSerializer(serializers.ModelSerializer):
  class Meta:
    model = Complaint
    fields ='__all__'

class RegisterComplaintSerializer(serializers.ModelSerializer):
  Time = serializers.DateField(format="%Y-%m-%d")
  class Meta:
    model = Complaint
    fields = ('Subject', 'user_name', 'contactnumber',
         'Type_of_complaint', 'Description', 'Time','status')
    extra_kwargs = {
      'user_name': {'required': True},
      'status': {'required': True},
      'contactnumber': {'required': True},
      'Description':{'required': True}
    }
  '''def validate(self, attrs):
    profile1=Profile.objects.all()
    if attrs['contactnumber']!=profile1['contactnumber']:
      raise serializers.ValidationError(
        {"contactnumber": "contactnumber didn't match."})
    return attrs'''
    
  def create(self, validated_data):
    complaint = Complaint.objects.create(
      user_name=validated_data['user_name'],
      contactnumber=validated_data['contactnumber'],
      status=validated_data['status'],
      Time=validated_data['Time'],
      Description=validated_data['Description'],
      Type_of_complaint=validated_data['Type_of_complaint'],
      Subject=validated_data['Subject'],
    )
    #profile.set_password(validated_data['password'])
    complaint.save()
    return complaint
