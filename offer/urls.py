from django.urls import path

from . import views

app_name = 'offer'

urlpatterns = [
    path('napravi/', views.new, name='new'),
    path('<int:pk>/', views.details, name='details'),
    path('<int:pk>/izmeni/', views.edit, name='edit'),
    path('<int:pk>/ukloni/', views.delete, name='delete'),
]
