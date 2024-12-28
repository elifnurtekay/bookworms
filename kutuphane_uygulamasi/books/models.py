# --- books/models.py ---
from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Book(models.Model):
    id = models.AutoField(primary_key=True)  # id alanı birincil anahtar olarak tanımlandı
    title = models.CharField(max_length=255)
    isbn = models.CharField(max_length=13, unique=True)
    publication_year = models.PositiveIntegerField()
    stock_status = models.PositiveIntegerField(default=1)
    categories = models.ManyToManyField(Category, related_name='books')

    def __str__(self):
        return self.title
