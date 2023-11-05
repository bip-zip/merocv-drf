from django.urls import path
from .views import UserDetailAPI,RegisterUserAPIView, UserLoginAPI

urlpatterns = [
  path('register',RegisterUserAPIView.as_view()),
  path("login",UserLoginAPI.as_view()),
]