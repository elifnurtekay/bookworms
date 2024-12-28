from django.urls import path
from . import views

app_name = 'notifications'

urlpatterns = [
    path('send-reminders/', views.trigger_notifications, name='send_reminders'),
]
