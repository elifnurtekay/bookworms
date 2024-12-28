# --- reviews/urls.py ---
from django.urls import path
from . import views

app_name = 'reviews'

urlpatterns = [
    #path('', views.list_reviews, name='list_reviews'),
    path('<int:book_id>/', views.list_reviews, name='list_reviews'),
    path('add/<int:book_id>/', views.add_review, name='add_review'),
]
