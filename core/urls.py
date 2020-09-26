from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('login/', views.loginUser, name="loginUser"),
    path('logout/', views.logoutUser, name="logoutUser"),    
    path('register/', views.registerUser, name="registerUser"),    
    path('', views.home, name="home"),
    path('delete/<str:pk>/', views.delete, name="delete"),
    path('reset_password/', auth_views.PasswordResetView.as_view(template_name="core/password_reset.html"), name="password_reset"),
    path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(template_name="core/password_reset_sent.html"), name="password_reset_done"),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name="core/reset_confirm.html"), name="password_reset_confirm"),
    path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(template_name="core/reset_complete.html"), name="password_reset_complete"),
]
