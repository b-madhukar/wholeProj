from rest_framework import serializers
from django.contrib.auth.models import User
from .models import ServiceStaff
from rest_framework.response import Response
from rest_framework import status
from rest_framework.validators import UniqueValidator
from django.contrib.auth.password_validation import validate_password

#Serializer to Get User Details using Django Token Authentication
class ServicestaffSerializer(serializers.ModelSerializer):
  class Meta:
    model = ServiceStaff
    fields ='__all__'

#Serializer to Register User
class ServicestaffRegisterSerializer(serializers.ModelSerializer):
  email_id = serializers.EmailField(
    required=True,
    validators=[UniqueValidator(queryset=ServiceStaff.objects.all())]
  )
  
  password = serializers.CharField(
    write_only=True, required=True, validators=[validate_password],style={'input_type': 'password', 'placeholder': 'Password'})
  password2 = serializers.CharField(
    write_only=True, required=True, validators=[validate_password],style={'input_type': 'password', 'placeholder': 'Password'})
  #password2 = serializers.CharField(write_only=True, required=True)
  class Meta:
    model = ServiceStaff
    fields = ('user_name', 'password', 'password2',
         'email_id', 'first_name', 'last_name','contactnumber','department')
    extra_kwargs = {
      'first_name': {'required': True},
      'last_name': {'required': True},
      'contactnumber': {'required': True},
      'Department':{'required': True}
    }
  def validate(self, attrs):
    if attrs['password'] != attrs['password2']:
      raise serializers.ValidationError(
        {"password": "Password fields didn't match."})
    return attrs
  def create(self, validated_data):
    servicestaff = ServiceStaff.objects.create(
      user_name=validated_data['user_name'],
      email_id=validated_data['email_id'],
      first_name=validated_data['first_name'],
      last_name=validated_data['last_name'],
      contactnumber=validated_data['contactnumber'],
      department=validated_data['department'],
      password=validated_data['password2']
    )
    #profile.set_password(validated_data['password'])
    servicestaff.save()
    return servicestaff
