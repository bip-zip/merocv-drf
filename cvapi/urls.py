from django.urls import path
from .views import UserInfoCreateUpdateView, WorkExperienceCreateView, EducationCreateView

urlpatterns = [
  path('userinfo',UserInfoCreateUpdateView.as_view()),
  path('experiences',WorkExperienceCreateView.as_view()),
  path('education',EducationCreateView.as_view()),
]