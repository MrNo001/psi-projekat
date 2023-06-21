from django.urls import path

from . import views

app_name = 'moderator'

urlpatterns = [
    path('panel/', views.panel, name='panel'),
    path('prijavi/', views.report, name='report'),
    path('razresi/', views.resolve, name='resolve'),
    # path('report_ad/', views.report_ad, name='report_ad'),
]