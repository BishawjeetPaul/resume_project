from django.urls import path
from . import views


urlpatterns = [
    path('my-services/', views.services, name='services'),
]
