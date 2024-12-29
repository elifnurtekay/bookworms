# --- books/models.py ---
from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Author(models.Model):
    name = models.CharField(max_length=255)
    

    def __str__(self):
        return self.name

class Book(models.Model):
    id = models.AutoField(primary_key=True)  # id alanı birincil anahtar olarak tanımlandı
    isbn = models.CharField(max_length=13, unique=True)
    title = models.CharField(max_length=255)
    publication_year = models.PositiveIntegerField()
    stock_status = models.PositiveIntegerField(default=1)
    categories = models.ManyToManyField(Category, related_name='books')
    main_author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='main_books')  # Ana yazar
    co_authors = models.ManyToManyField(Author, related_name='coauthored_books', blank=True)  # Yardımcı yazarlar

    def __str__(self):
        return self.title
