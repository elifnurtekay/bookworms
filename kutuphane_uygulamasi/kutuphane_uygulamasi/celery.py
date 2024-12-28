from __future__ import absolute_import, unicode_literals
import os
from celery import Celery

# Django'nun ayarlarını Celery'ye yükleme
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'kutuphane_uygulamasi.settings')

app = Celery('kutuphane_uygulamasi')

# Ayarları projeden çek
app.config_from_object('django.conf:settings', namespace='CELERY')

# Görevlerin otomatik olarak algılanması
app.autodiscover_tasks()
