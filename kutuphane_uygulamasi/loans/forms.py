# --- loans/forms.py ---
from django import forms
from .models import Loan

class LoanForm(forms.ModelForm):
    class Meta:
        model = Loan
        fields = []  # Kullanıcı ve kitap bilgileri otomatik atanacak

