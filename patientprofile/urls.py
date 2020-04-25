from django.urls import path

from patientprofile import views

urlpatterns = [
    path('', views.patient, name='patient_profile'),
]