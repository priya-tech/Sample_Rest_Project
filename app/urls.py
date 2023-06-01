from django.urls import path
from app import views

urlpatterns = [
    path('users_list', views.UserList, name='users_list'),
    path('user_create', views.CreateUser, name='user_create'),
    path('user_detail/<pk>', views.UserDetail, name='user_detail'),
]