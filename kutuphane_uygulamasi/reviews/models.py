# --- reviews/models.py ---
from django.db import models
from django.conf import settings
from books.models import Book
from users.models import CustomUser

class Review(models.Model):
    id = models.AutoField(primary_key=True)  # id alanı birincil anahtar olarak tanımlandı
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='reviews')   #isbn
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='reviews')
    rating = models.PositiveIntegerField()  # Puanlama 1-5 arası olabilir
    comment = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'book')  # Kullanıcı ve kitap kombinasyonu benzersiz olmalı

    """class Meta:
    constraints = [
        models.UniqueConstraint(fields=['user', 'book'], name='unique_user_book_review')
    ]
"""

    def __str__(self):
        return f"{self.book.title} - {self.user.username}"   
    
    #def __str__(self):
       # return f"{self.book.title} - {self.user.get_username()}"

