# Define URL patterns for articles

from django.urls import path
from django.contrib.auth.views import LoginView  # Use LoginView for login
from . import views

urlpatterns = [
    # Login page
    path('login/', LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', views.logout_view, name='logout'), 
    # Registration page
    path('register/', views.register, name='register'),
]