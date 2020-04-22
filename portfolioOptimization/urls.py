from django.urls import path,re_path
from . import views

urlpatterns = [
path('optimize/', views.optimize, name='optimize'),
path('Suggest/', views.suggest, name='getSuggestion'),
path('showResults/', views.result, name='results'),
]