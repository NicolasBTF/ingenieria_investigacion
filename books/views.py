# books/views.py

from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from .models import Category, Book

def index(request):
    categories = Category.objects.all()
    featured_books = Book.objects.filter(featured=True, available=True)[:6]
    latest_books = Book.objects.filter(available=True)[:12]
    
    context = {
        'categories': categories,
        'featured_books': featured_books,
        'latest_books': latest_books,
    }
    
    return render(request, 'books/index.html', context)

def book_detail_json(request, slug):
    book = get_object_or_404(Book, slug=slug, available=True)
    
    # Preparamos los datos del libro para enviar como JSON
    book_data = {
        'id': book.id,
        'title': book.title,
        'author': book.author.name,
        'description': book.description,
        'price': float(book.price),
        'isbn': book.isbn,
        'pages': book.pages,
        'cover_url': book.cover.url if book.cover else '',
        'publication_date': book.publication_date.strftime('%d/%m/%Y') if book.publication_date else '',
        'categories': [category.name for category in book.categories.all()]
    }
    
    return JsonResponse(book_data)

def category_books(request, category_slug):
    category = get_object_or_404(Category, slug=category_slug)
    books = Book.objects.filter(categories=category, available=True)
    
    context = {
        'category': category,
        'books': books,
    }
    
    return render(request, 'books/category_books.html', context)
