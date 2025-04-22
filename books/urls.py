# books/urls.py

from django.urls import path
from . import views

app_name = 'books'

urlpatterns = [
    path('', views.index, name='index'),
    path('libro/<slug:slug>/json/', views.book_detail_json, name='book_detail_json'),
    path('categoria/<slug:category_slug>/', views.category_books, name='category_books'),
]

