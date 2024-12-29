# --- loans/models.py ---
from django.db import models
from users.models import CustomUser
from books.models import Book

class Loan(models.Model):
    id = models.AutoField(primary_key=True)  # id alanı birincil anahtar olarak tanımlandı
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='loans')
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='loans')
    loan_date = models.DateField(auto_now_add=True)
    due_date = models.DateField()
    returned = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.user.username} - {self.book.title}"
