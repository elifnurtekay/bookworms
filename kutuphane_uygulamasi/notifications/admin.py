#from django.contrib import admin

# Register your models here.
# --- notifications/admin.py ---
# Eğer notifications için bir model kullanılıyorsa:
from django.contrib import admin
# from .models import Notification  # Model varsa açın

# @admin.register(Notification)
# class NotificationAdmin(admin.ModelAdmin):
#     list_display = ('user', 'message', 'created_at')
#     list_filter = ('created_at',)
#     search_fields = ('user__username', 'message')
#     ordering = ('-created_at',)

# Eğer yalnızca görevler çalıştırılıyorsa, admin.py'ye ekleme yapmanız gerekmez.