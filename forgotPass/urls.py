from django.urls import path
from . import views

urlpatterns = [
    path('', views.forgotPass, name='forgot-Pass'),
]