from django.urls import path

from . import views

urlpatterns = [
    path('', views.symptom, name='symptom'),
]
