from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import UserInfo, WorkExperience, Education, Certification, SkillHighlight
from .serializers import UserInfoSerializer, WorkExperienceSerializer, EducationSerializer, CertificationSerializer, SkillHighlightSerializer

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
            education = Education.objects.filter(user=request.user)
            serializer = EducationSerializer(education, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except UserInfo.DoesNotExist:
            return Response(
                {"detail": "User information not found."},
                status=status.HTTP_404_NOT_FOUND
            )


class CertificationCreateView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        print(request.data)
        serializer = CertificationSerializer(data=request.data, context={'request': request})

        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def get(self, request, *args, **kwargs):
        try:
            certifications = Certification.objects.filter(user=request.user)
            serializer = CertificationSerializer(certifications, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except UserInfo.DoesNotExist:
            return Response(
                {"detail": "User information not found."},
                status=status.HTTP_404_NOT_FOUND
            )

class SkillHighlightCreateView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        print(request.data)
        serializer = SkillHighlightSerializer(data=request.data, context={'request': request})

        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def get(self, request, *args, **kwargs):
        try:
            skillhighlight = SkillHighlight.objects.filter(user=request.user)
            serializer = SkillHighlightSerializer(skillhighlight, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except UserInfo.DoesNotExist:
            return Response(
                {"detail": "User information not found."},
                status=status.HTTP_404_NOT_FOUND
            )
