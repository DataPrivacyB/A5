from django.urls import path
from . import views

from pred_app import views

urlpatterns = [

    path('index', views.index, name='index'),
    path('about', views.about, name='about'),
    path('home', views.home, name='home'),
    path('prediction', views.prediction, name='prediction'),

    path('clustering/', views.clustering, name='clustering'),
    path('scrape/', views.scrape, name='scrape'),
    path('sharevaluedetermine/', views.sharevaluedetermine, name='sharevaluedetermine'),
    path('logout/', views.logout, name='logout'),

    path('portfolio/', views.portfolio, name='portfolio'),
    path('profile/', views.profile, name='profile'),
##    path('login/', auth_views.LoginView.as_view(template_name='pred_app/login.html'), name='login'),

]
