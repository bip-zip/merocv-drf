from rest_framework import serializers
from .models import UserInfo, Resume, Education, WorkExperience, Certification, SkillHighlight

class UserInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserInfo
        fields = '__all__'
        read_only_fields = ('user',)  # Make the 'user' field read-only

    def create(self, validated_data):
        request = self.context.get('request')
        if request:
            user = request.user
            validated_data['user'] = user
            return UserInfo.objects.create(**validated_data)
        else:
            raise ValueError("Request context not available in the serializer.")

class ResumeSerializer(serializers.ModelSerializer):
    user = UserInfoSerializer()  # Include UserInfo fields using UserInfoSerializer

    class Meta:
        model = Resume
        fields = '__all__'

class EducationSerializer(serializers.ModelSerializer):
    resumeid = ResumeSerializer()

    class Meta:
        model = Education
        fields = '__all__'

class WorkExperienceSerializer(serializers.ModelSerializer):
    resumeid = ResumeSerializer()

    class Meta:
        model = WorkExperience
        fields = '__all__'

class CertificationSerializer(serializers.ModelSerializer):
    resumeid = ResumeSerializer()

    class Meta:
        model = Certification
        fields = '__all__'

class SkillHighlightSerializer(serializers.ModelSerializer):
    resumeid = ResumeSerializer()

    class Meta:
        model = SkillHighlight
        fields = '__all__'
