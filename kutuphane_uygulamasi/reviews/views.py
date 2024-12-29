# --- reviews/views.py ---
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Review
from loans.models import Loan
from books.models import Book
from users.models import CustomUser
from .forms import ReviewForm

@login_required
def add_review(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    
    # Kullanıcının bu kitabı ödünç alıp almadığını kontrol et
    loan_exists = Loan.objects.filter(user=request.user, book=book, returned=True).exists()
    if not loan_exists:
        messages.error(request, "Bu kitabı daha önce ödünç almadığınız için yorum yapamazsınız.")
        return redirect('reviews:list_reviews', book_id=book.id)

    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.user = request.user
            review.book = book
            review.save()
            messages.success(request, "Yorumunuz başarıyla eklendi.")
            return redirect('reviews:list_reviews', book_id=book.id)
    else:
        form = ReviewForm()
    
    return render(request, 'add_review.html', {'form': form, 'book': book})


@login_required
def list_reviews(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    reviews = book.reviews.all()

    # Kullanıcının bu kitabı ödünç alıp almadığını kontrol et
    loan_exists = Loan.objects.filter(user=request.user, book=book, returned=True).exists()

    return render(request, 'list_reviews.html', {
        'book': book,
        'reviews': reviews,
        'loan_exists': loan_exists  # Sonucu şablona gönder
    })







"""@login_required
def list_reviews(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    reviews = book.reviews.all()
    return render(request, 'list_reviews.html', {'book': book, 'reviews': reviews})"""