from django.urls import path

from . import views
from moderator import views as modViews

app_name = 'offer'

urlpatterns = [
    path('napravi/', views.new, name='new'),
    path('<int:pk>/', views.details, name='details'),
    path('<int:pk>/izmeni/', views.edit, name='edit'),
    path('<int:pk>/ukloni/', views.delete, name='delete'),
    path('<int:pk>/zaprati/', views.follow, name='follow'),
    path('<int:pk>/odprati/', views.unfollow, name='unfollow'),
    # path('follow_ad/', views.follow_ad, name='follow_ad'),
]
