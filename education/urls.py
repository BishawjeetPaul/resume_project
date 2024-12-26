from django.urls import path
from . import views


urlpatterns = [
    path('mySkills/', views.skills, name='skills'),
]
