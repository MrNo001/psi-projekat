from django.urls import path

from . import views

app_name = 'company'

urlpatterns = [
    path('plac/<str:firm_name>/', views.plac, name='plac'),
    path('plac/<str:firm_name>/oceni', views.rate, name='rate'),
    # path('plac/<str:name>/reviews', views.reviews , name='reviews')
]
