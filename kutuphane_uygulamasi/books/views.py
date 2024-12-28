from django.shortcuts import render, get_object_or_404, redirect
from .models import Book
from .forms import BookForm
from django.http import HttpResponseForbidden

def list_books(request):
    books = Book.objects.all()
    return render(request, 'list_books.html', {'books': books})

def add_book(request):
    if not request.user.is_authenticated or not request.user.is_library_admin:
        return HttpResponseForbidden("Bu işlemi gerçekleştirme yetkiniz yok.")

    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('books:list_books')
    else:
        form = BookForm()
    return render(request, 'add_book.html', {'form': form})

def update_book(request, id):
    book = get_object_or_404(Book, id=id)
    if request.method == 'POST':
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('books:list_books')  # Namespace eklendi
    else:
        form = BookForm(instance=book)
    return render(request, 'update_book.html', {'form': form, 'book': book})

def delete_book(request, id):
    book = get_object_or_404(Book, id=id)
    if request.method == 'POST':
        book.delete()
        return redirect('books:list_books')  # Namespace eklendi
    return render(request, 'delete_book.html', {'book': book})
