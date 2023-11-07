from django.urls import path
from .views import UserInfoCreateUpdateView

urlpatterns = [
  path('userinfo',UserInfoCreateUpdateView.as_view()),
 
]