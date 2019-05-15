from django.urls import path
from basicsApp import views


# TEMPLATE URLS

app_name = 'basicsApp'

urlpatterns = [

    path('register/', views.register, name='register'),
    path('user_login/', views.user_login, name='user_login')
]