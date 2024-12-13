# help/urls.py

from django.urls import path
from .views import post_list, register, post_create, delete_post
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', post_list, name='post_list'),
    path('register/', register, name='register'),
    path('post/create/', post_create, name='post_create'),
    path('post/<int:post_id>/delete/', delete_post, name='delete_post'),
    path('login/', auth_views.LoginView.as_view(template_name='help/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]