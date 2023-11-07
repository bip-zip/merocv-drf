from django.db import models
from django.contrib.auth.models import User

class UserInfo(models.Model):
    user = models.OneToOneField(User, primary_key=True, on_delete=models.CASCADE)
    contact = models.CharField(max_length=10)
    email = models.EmailField()
    image = models.ImageField(upload_to='user_images/')
    address = models.CharField(max_length=499)
    summary = models.TextField(null=True)

    def __str__(self) -> str:
        return self.user.username

class Resume(models.Model):
    date_created = models.DateField(auto_created=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.user.username

class Education(models.Model):
    institution = models.CharField(max_length=499)
    address = models.CharField(max_length=499)
    degree = models.CharField(max_length=300)
    completion_date = models.DateField()
    grade = models.CharField(max_length=3)
    percentage = models.PositiveSmallIntegerField()
    resumeid = models.ForeignKey(Resume, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.institution

class WorkExperience(models.Model):
    company = models.CharField(max_length=100)
    address = models.CharField(max_length=499)
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)
    role = models.CharField(max_length=30)
    responsibility = models.CharField(max_length=500)
    resumeid = models.ForeignKey(Resume, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.company


class Certification(models.Model):
    institution = models.CharField(max_length=499)
    address = models.CharField(max_length=499)
    degree = models.CharField(max_length=300)
    completion_date = models.DateField()
    grade = models.CharField(max_length=3)
    percentage = models.PositiveSmallIntegerField()
    resumeid = models.ForeignKey(Resume, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.institution

class SkillHighlight(models.Model):
    skill = models.CharField(max_length=70)
    level = models.CharField(max_length=20)
    resumeid = models.ForeignKey(Resume, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.skill

