import email
from django.shortcuts import render
from django.http import JsonResponse

from rest_framework.decorators import api_view
from rest_framework.response import Response
# Create your views here.
@api_view(['GET'])
def apiOverview(request):
    return JsonResponse("Hello API",safe =False)
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView
from rest_framework.response import Response
from client.serializers import UserSerializer
from .serializers import RegisterSerializer
from django.contrib.auth.models import User
from rest_framework.authentication import TokenAuthentication
from rest_framework import generics
from .models import Profile

# Class based view to Get User Details using Token Authentication
class UserDetailAPI(APIView):
  authentication_classes = (TokenAuthentication,)
  permission_classes = (AllowAny,)
  '''def get(self,request,*args,**kwargs):
    all_users = Profile.objects.values()
    print(all_users)
    profile = Profile.objects.all()
    serializer = UserSerializer(profile)
    return Response(all_users)'''
  def get(self,request):
      email = request.query_params.get('email')
      pwd=request.query_params.get('pwd')
      print(email)
      print(pwd)
      try:
        user = Profile.objects.get(email_id=email)
        serializer = UserSerializer(user)
        pwdval=serializer['password'].value
        if pwd==pwdval :
          return JsonResponse(serializer.data,safe=False)
        else:
          return JsonResponse("Invalid Credentials",safe=False)
      except:
        return JsonResponse("Invalid Detials",safe=False)

    
   

#Class based view to register user
class RegisterUserAPIView(generics.CreateAPIView):
  permission_classes = (AllowAny,)
  serializer_class = RegisterSerializer