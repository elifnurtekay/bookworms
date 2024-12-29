# --- loans/admin.py ---
from django.contrib import admin
from .models import Loan

@admin.register(Loan)
class LoanAdmin(admin.ModelAdmin):
    list_display = ('user', 'book', 'loan_date', 'due_date', 'returned')
    list_filter = ('returned', 'due_date')
    search_fields = ('user__username', 'book__title')
    ordering = ('due_date',)
