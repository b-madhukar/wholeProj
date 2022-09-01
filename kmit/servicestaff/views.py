from django.shortcuts import render
from django.http import JsonResponse

from rest_framework.decorators import api_view
from rest_framework.response import Response
# Create your views here.
@api_view(['GET'])
def servicestaffapiOverview(request):
    return JsonResponse("Hello API",safe =False)
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView
from rest_framework.response import Response
from servicestaff.serializers import ServicestaffSerializer
from .serializers import ServicestaffRegisterSerializer
from django.contrib.auth.models import User
from rest_framework.authentication import TokenAuthentication
from rest_framework import generics
from .models import ServiceStaff

# Class based view to Get User Details using Token Authentication
class ServicestaffDetailAPI(APIView):
  authentication_classes = (TokenAuthentication,)
  permission_classes = (AllowAny,)
  def get(self,request,*args,**kwargs):
    servicestaff = ServiceStaff.objects.get(id=request.user.id)
    serializer = ServicestaffSerializer(servicestaff)
    return Response(serializer.data)

#Class based view to register user
class RegisterServicestaffAPIView(generics.CreateAPIView):
  permission_classes = (AllowAny,)
  serializer_class = ServicestaffRegisterSerializer