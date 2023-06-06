from django.urls import path

from . import views

app_name = 'moderator'

urlpatterns = [
    path('panel/', views.panel, name='panel'),
]