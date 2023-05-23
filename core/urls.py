from django.contrib.auth import views as auth_views 
from django.urls import path
from. import views
from. forms import LoginForm

app_name = 'core'

urlpatterns = [
    path('', views.home, name= 'home'),
    path('loginPage/', views.loginPage, name='loginPage'),
    path('logoutUser/', views.logoutUser, name='logoutUser'),
    path('profile/', views.profile, name='profile'),
   
    path('contact/', views.contact, name= 'contact'),
    path('signUp/', views.signUp, name= 'signUp'),
    
    path('login/', auth_views.LoginView.as_view(template_name = 'core/login.html', authentication_form = LoginForm),name='login' )
]