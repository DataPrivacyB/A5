from django.urls import path,re_path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    #path('forgotPass/', views.forgotPass, name='forgot-Pass'),
    path('password_reset/', auth_views.PasswordResetView.as_view(template_name='userRegistration/password_reset_form.html'), name='password_reset' ),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='userRegistration/password_reset_done.html'), name='password_reset_done' ),
    re_path(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        auth_views.PasswordResetConfirmView.as_view(
            template_name='userRegistration/password_reset_confirm.html')
            , name='password_reset_confirm' ),

    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='userRegistration/password_reset_complete.html'), name='password_reset_complete' ),
    path('login/',auth_views.LoginView.as_view(template_name='userRegistration/login.html'),name='login'),
    path('edituser/', views.edituser, name='edituser'),
    path('logout/',auth_views.LogoutView.as_view(template_name='userRegistration/logout.html'),name='logout'),
    path('profile/', views.about, name='profile'),
    path('registration/', views.index, name='registration'),
    path('registration/registered', views.registered, name='registered'),
    path('about/', views.about, name='about'),
    path('portfolio/', views.portfolio, name='portfolio'),
    path('Home/', views.Home, name='Home'),
    path('AboutProject/', views.AboutProject, name='AboutProject'),
path('practice/', views.practice, name='practice'),
]