from django.urls import path

from . import views

app_name = 'offer'

urlpatterns = [
    path('napravi/', views.new, name='new'),
    path('<int:pk>/', views.detail, name='detail'),
    path('<int:pk>/delete/', views.delete, name='delete'),
    path('<int:pk>/izmeni/', views.edit, name='edit'),
]
