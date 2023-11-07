from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import UserInfo, WorkExperience, Education
from .serializers import UserInfoSerializer, WorkExperienceSerializer, EducationSerializer

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
    
    def get(self, request, *args, **kwargs):
        try:
            user_info = UserInfo.objects.get(user=request.user)
            serializer = UserInfoSerializer(user_info)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except UserInfo.DoesNotExist:
            return Response(
                {"detail": "User information not found."},
                status=status.HTTP_404_NOT_FOUND
            )

class WorkExperienceCreateView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        print(request.data)
        serializer = WorkExperienceSerializer(data=request.data, context={'request': request})

        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def get(self, request, *args, **kwargs):
        try:
            work_experiences = WorkExperience.objects.filter(user=request.user)
            serializer = WorkExperienceSerializer(work_experiences, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except UserInfo.DoesNotExist:
            return Response(
                {"detail": "User information not found."},
                status=status.HTTP_404_NOT_FOUND
            )
        
class EducationCreateView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        print(request.data)
        serializer = EducationSerializer(data=request.data, context={'request': request})

        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def get(self, request, *args, **kwargs):
        try:
            work_experiences = Education.objects.filter(user=request.user)
            serializer = EducationSerializer(work_experiences, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except UserInfo.DoesNotExist:
            return Response(
                {"detail": "User information not found."},
                status=status.HTTP_404_NOT_FOUND
            )

