from django.contrib.auth import views as auth_views
from django.urls import path

from . import views
from moderator import views as v

app_name = 'search'

urlpatterns = [
    path('', views.index, name='home'),
    path('pretraga/', views.browse, name='browse'),
    path('o-nama/', views.about, name='about'),
    # path('pretraga/report_ad/', v.report_ad, name='report_ad'),
    # path('pretraga/follow_ad/', v.follow_ad, name='follow_ad'),
]