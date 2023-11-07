from django.urls import path
from .views import UserInfoCreateUpdateView, WorkExperienceCreateView, EducationCreateView,CertificationCreateView, SkillHighlightCreateView

urlpatterns = [
  path('userinfo',UserInfoCreateUpdateView.as_view()),
  path('experiences',WorkExperienceCreateView.as_view()),
  path('education',EducationCreateView.as_view()),
  path('certifications',CertificationCreateView.as_view()),
  path('skills',SkillHighlightCreateView.as_view()),
]