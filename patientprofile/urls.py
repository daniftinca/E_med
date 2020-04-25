from django.urls import path

from patientprofile import views

urlpatterns = [
    path('', views.profile, name='profile'),
]