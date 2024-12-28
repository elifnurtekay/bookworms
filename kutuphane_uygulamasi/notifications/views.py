from django.http import HttpResponse
from .tasks import send_due_date_reminders

def trigger_notifications(request):
    send_due_date_reminders()
    return HttpResponse("Bildirimler gönderildi.")
