from django import views
from django.urls import path
from complaints.views import ComplaintDetailAPI,RegisterComplaintAPIView
from django.urls import include, path
from . import views
urlpatterns = [
  path("get-complaint-details",ComplaintDetailAPI.as_view()),
  path('register-complaint',RegisterComplaintAPIView.as_view()),
  
]
