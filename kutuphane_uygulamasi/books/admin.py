# --- books/admin.py ---
from django.contrib import admin
from .models import Book
from .models import Category
from .models import Author

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('name',)

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'main_author', 'publication_year', 'stock_status')
    list_filter = ('categories',)
    search_fields = ('title', 'isbn')
    filter_horizontal = ('categories', 'co_authors')  # co_authors alanı için çoklu seçim özelliği

"""@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'isbn', 'stock_status')
    search_fields = ('title', 'isbn')
    ordering = ('title',)"""
