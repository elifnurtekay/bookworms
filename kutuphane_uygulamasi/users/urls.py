# --- users/urls.py ---
from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register_user, name='register_user'),
    path('login/', views.login_user, name='login_user'),
    path('admin-login/', views.login_library_admin, name='login_library_admin'),
    path('logout/', views.logout_user, name='logout_user'),
]