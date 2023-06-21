from django.urls import path

from . import views

app_name = 'moderator'

urlpatterns = [
    path('panel/', views.panel, name='panel'),
    path('report_ad/', views.report_ad, name='report_ad'),
    path('oglas/<int:pk>/prijavi/', views.report, name='report'),
    path('oglas/<int:pk>/razresi/', views.resolve, name='resolve'),
]