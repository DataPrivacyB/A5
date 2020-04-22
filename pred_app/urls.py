from django.urls import path
from . import views

from pred_app import views

urlpatterns = [

    path('index', views.index, name='index'),
    path('pred', views.pred, name='pred'),
    path('contact', views.contact, name='contact'),
    path('AboutProject', views.AboutProject, name='AboutProject'),
    path('home', views.home, name='home'),
    path('lstm_prediction', views.lstm_prediction, name='lstm_prediction'),

    path('portfolio/', views.portfolio, name='portfolio'),
    path('profile/', views.profile, name='profile'),
##    path('login/', auth_views.LoginView.as_view(template_name='pred_app/login.html'), name='login'),

]
