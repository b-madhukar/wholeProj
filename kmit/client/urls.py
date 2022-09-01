from django import views
from django.urls import path
from client.views import UserDetailAPI,RegisterUserAPIView
from django.urls import include, path
from . import views
urlpatterns = [
  path("get-details",UserDetailAPI.as_view()),
  path('register',RegisterUserAPIView.as_view()),
  path('api/', views.apiOverview, name='main-view'),
]
