from django.urls import path

from . import views

urlpatterns = [
    path('', views.doctor, name='doctor_profile'),
    path('speciality/', views.speciality, name='speciality'),
]
