from django.urls import path
from . import views
from .forms import LoginForm
from django.contrib.auth import views as auth_views

app_name = 'account'

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('registracija/', views.signup, name='signup'),
    path('login/', auth_views.LoginView.as_view(template_name='account/login.html', authentication_form=LoginForm), name='login'),
    path('profil/',views.dashboard,name='dashboard'),
    path('logout/',views.logoutuser,name='logoutuser')
]
