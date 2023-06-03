from django.contrib.auth import views as auth_views
from django.urls import path

from . import views

app_name = 'search'

urlpatterns = [
    path('', views.index, name='home'),
    path('pretraga/', views.browse, name='browse'),
    path('o-nama/', views.about, name='about'),
]