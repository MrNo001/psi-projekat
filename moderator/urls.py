from django.urls import path

from . import views

app_name = 'conversation'

urlpatterns = [
    path('panel/', views.panel, name='panel'),
]