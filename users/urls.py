from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', auth_views.LoginView.as_view(
        redirect_authenticated_user=True), name='login'),
    path('processlogin', views.process_login, name='processlogin'),
    path('logout', auth_views.LogoutView.as_view(), name='logout'),
    path('register', views.register_user, name='register'),
]
