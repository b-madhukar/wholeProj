from django import views
from django.urls import path
from servicestaff.views import ServicestaffDetailAPI,RegisterServicestaffAPIView
from django.urls import include, path
from . import views
from servicestaff.views import servicestaffapiOverview
urlpatterns = [
  path("servicestaffget-details",ServicestaffDetailAPI.as_view()),
  path('servicestaffregister',RegisterServicestaffAPIView.as_view()),
  
]
