from django.urls import path
from . import views
from .views import *
from django.conf import settings

app_name = 'data'

urlpatterns = [
    path('', views.index, name='index'),
    path('submitdata', views.submit, name='submit'),
    path('data', forecast_data.as_view(), name='forecast_data'),
]
