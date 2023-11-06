from rest_framework.permissions import AllowAny
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import UserSerializer,RegisterSerializer,LoginSerializer
from django.contrib.auth.models import User
from rest_framework.authentication import TokenAuthentication
from rest_framework import generics
from django.views.generic import TemplateView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate

class HomeView(TemplateView):
    template_name = "index.html"


class RegisterUserAPIView(generics.CreateAPIView):
  permission_classes = (AllowAny,)
  serializer_class = RegisterSerializer

  def create(self, request, *args, **kwargs):
      serializer = self.get_serializer(data=request.data)
      serializer.is_valid(raise_exception=True)  
      username = request.data.get('username')

    # Check if the username already exists
      if User.objects.filter(username=username).exists():
        return Response({'message': 'Email already exists.'}, status=status.HTTP_200_OK)

      elif not self.validate_passwords(request.data):
        return Response({"message": "Password fields didn't match."}, status=status.HTTP_400_BAD_REQUEST)

      user = serializer.save()
      user.set_password(request.data.get('password'))
      user.save()
      return Response({'message': 'User created successfully','username':user.username}, status=status.HTTP_200_OK)

  def validate_passwords(self, data):
      if data.get('password') != data.get('password2'):
          return False
      return True


class UserLoginAPI(APIView):
    serializer_class = LoginSerializer
    def post(self, request, *args, **kwargs):
        username = request.data.get("username")
        password = request.data.get("password")
        
        user = authenticate(username=username, password=password)
        
        if user is not None:
            token, created = Token.objects.get_or_create(user=user)
            return Response({"token": token.key}, status=status.HTTP_200_OK)
        else:
            return Response({"error": "Invalid credentials"}, status=status.HTTP_401_UNAUTHORIZED)


class UserDetailAPI(APIView):
  authentication_classes = (TokenAuthentication,)
  permission_classes = (AllowAny,)

  def get(self,request,*args,**kwargs):
    user = User.objects.get(id=request.user.id)
    serializer = UserSerializer(user)
    return Response(serializer.data)



