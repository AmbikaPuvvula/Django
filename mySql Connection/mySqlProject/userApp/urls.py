from django.urls import path,include
from userApp import views
from django.contrib.auth import views as auth_views

urlpatterns=[
	path('signup/',views.signup,name='signup'),
	path('home/',views.home,name='home'),
	path('signin/',auth_views.LoginView.as_view(template_name='userApp/login.html'),name='login'),
	path('signout/',auth_views.LogoutView.as_view(template_name='userApp/logout.html'),name='logout'),
]