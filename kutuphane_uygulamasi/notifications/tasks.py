from celery import shared_task
from datetime import date, timedelta
from django.core.mail import send_mail
from django.conf import settings
from loans.models import Loan

@shared_task
def send_due_date_reminders():
    """
    Teslim tarihi yaklaşan kitaplar için kullanıcılara e-posta gönderen görev.
    """
    reminder_date = date.today() + timedelta(days=3)
    loans = Loan.objects.filter(due_date__lte=reminder_date, returned=False)

    for loan in loans:
        user = loan.user
        book = loan.book
        due_date = loan.due_date

        send_mail(
            subject='Teslim Tarihi Yaklaşıyor!',
            message=f"Merhaba {user.username},\n\n"
                    f"{book.title} adlı kitabınızın teslim tarihi {due_date}.\n"
                    f"Lütfen zamanında iade ettiğinizden emin olun.",
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=[user.email],
        )
