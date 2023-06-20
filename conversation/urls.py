from django.urls import path

from . import views

app_name = 'conversation'

urlpatterns = [
    path('', views.inbox, name='inbox'),
    path('<int:pk>/', views.details, name='details'),
    path('nova/<int:offer_pk>/', views.new_conversation, name='new'),
]
