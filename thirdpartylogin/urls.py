from django.urls import path

from thirdpartylogin import views
from thirdpartylogin.views import FacebookLogin
app_name = 'thirdpartylogin'
urlpatterns = [
    path('facebook/', FacebookLogin.as_view(), name='fb_login'),
    path('', views.user_register, name='user_register'),
]
