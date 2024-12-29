# --- loans/views.py ---
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from .models import Loan
from books.models import Book
from .forms import LoanForm
from datetime import timedelta, date

def list_loans(request):
    loans = Loan.objects.filter(user=request.user, returned=False)  # Kullanıcının aktif ödünç kitaplarını listeler
    return render(request, 'list_loans.html', {'loans': loans})

def select_book_for_borrow(request):
    books = Book.objects.filter(stock_status__gt=0)  # Stokta olan kitapları getir
    return render(request, 'select_book_for_borrow.html', {'books': books})

def borrow_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    if book.stock_status <= 0:
        messages.error(request, "Bu kitap şu anda mevcut değil.")
        return redirect('loans:select_book_for_borrow')

    if request.method == 'POST':
        form = LoanForm(request.POST)
        if form.is_valid():
            loan = form.save(commit=False)
            loan.user = request.user
            loan.book = book
            loan.due_date = date.today() + timedelta(days=2)  # Teslim süresi 14 gün
            loan.save()

            # Kitap stok durumunu güncelle
            book.stock_status -= 1
            book.save()

            messages.success(request, f"{book.title} başarıyla ödünç alındı. Teslim tarihi: {loan.due_date}")
            return redirect('books:list_books')
    else:
        form = LoanForm()
    return render(request, 'borrow_book.html', {'form': form, 'book': book})

def return_book(request, loan_id):
    loan = get_object_or_404(Loan, id=loan_id, user=request.user)

    if request.method == 'POST':
        loan.returned = True
        loan.save()

        # Kitap stok durumunu güncelle
        book = loan.book
        book.stock_status += 1
        book.save()

        messages.success(request, f"{loan.book.title} başarıyla iade edildi.")
        return redirect('books:list_books')

    return render(request, 'return_book.html', {'loan': loan})