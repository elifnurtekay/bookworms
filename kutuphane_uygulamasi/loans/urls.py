# --- loans/urls.py ---
from django.urls import path
from . import views

app_name = 'loans'  # Namespace tanımı

urlpatterns = [
    path('', views.list_loans, name='list_loans'),  # loans/ yolunu listeleme işlemiyle eşleştiriyoruz
    path('borrow/<int:book_id>/', views.borrow_book, name='borrow_book'),
    path('return/<int:loan_id>/', views.return_book, name='return_book'),
    path('select/', views.select_book_for_borrow, name='select_book_for_borrow'), 
]