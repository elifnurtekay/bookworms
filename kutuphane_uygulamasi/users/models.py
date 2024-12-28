from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models

class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)
    is_library_admin = models.BooleanField(default=False)  # Kütüphane yöneticisi için ek alan
    date_joined = models.DateTimeField(auto_now_add=True)

    # Çakışmayı önlemek için related_name ekliyoruz
    groups = models.ManyToManyField(
        Group,
        related_name='customuser_groups',
        blank=True
    )
    user_permissions = models.ManyToManyField(
        Permission,
        related_name='customuser_permissions',
        blank=True
    )

    def __str__(self):
        return self.username

