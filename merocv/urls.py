
from django.contrib import admin
from django.urls import path,include
from rest_framework.authtoken import views
from userauth.views import HomeView

urlpatterns = [
  path('admin/', admin.site.urls),
  path('',HomeView.as_view()),
  path('auth/',include('userauth.urls')),
  path('cv/',include('cvapi.urls')),
  path('api-token-auth', views.obtain_auth_token)
]
