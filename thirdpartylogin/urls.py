from django.contrib.auth import login
from django.urls import path

from thirdpartylogin import views
from thirdpartylogin.views import FacebookLogin
app_name = 'thirdpartylogin'
urlpatterns = [
    path('facebook/', FacebookLogin.as_view(), name='fb_login'),
    path('register/', views.user_register, name='user_register'),
    path('login/', login, name='user_register'),
]
