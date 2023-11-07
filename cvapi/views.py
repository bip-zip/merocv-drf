from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import UserInfo
from .serializers import UserInfoSerializer

class UserInfoCreateUpdateView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        try:
            # Retrieve the UserInfo object for the authenticated user
            user_info = UserInfo.objects.get(user=request.user)
            serializer = UserInfoSerializer(user_info, data=request.data)
        except UserInfo.DoesNotExist:
            serializer = UserInfoSerializer(data=request.data, context={'request': request})

        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
