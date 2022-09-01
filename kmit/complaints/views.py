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
from complaints.serializers import ComplaintSerializer
from .serializers import RegisterComplaintSerializer
from django.contrib.auth.models import User
from rest_framework.authentication import TokenAuthentication
from rest_framework import generics
from .models import Complaint

# Class based view to Get User Details using Token Authentication
class ComplaintDetailAPI(APIView):
  permission_classes = (AllowAny,)
  def get(self,request,*args,**kwargs):
    complaint = Complaint.objects.get(id=request.user.id)
    serializer = ComplaintSerializer(complaint)
    return Response(serializer.data)

#Class based view to register user
class RegisterComplaintAPIView(generics.CreateAPIView):
  permission_classes = (AllowAny,)
  serializer_class = RegisterComplaintSerializer