# books/models.py

from django.db import models
from django.urls import reverse

class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name='Categoría')
    slug = models.SlugField(unique=True, verbose_name='Slug')
    
    class Meta:
        verbose_name = 'Categoría'
        verbose_name_plural = 'Categorías'
        ordering = ['name']
    
    def __str__(self):
        return self.name

class Author(models.Model):
    name = models.CharField(max_length=200, verbose_name='Nombre')
    bio = models.TextField(blank=True, verbose_name='Biografía')
    
    class Meta:
        verbose_name = 'Autor'
        verbose_name_plural = 'Autores'
        ordering = ['name']
    
    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=200, verbose_name='Título')
    slug = models.SlugField(unique=True, verbose_name='Slug')
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='books', verbose_name='Autor')
    categories = models.ManyToManyField(Category, related_name='books', verbose_name='Categorías')
    description = models.TextField(verbose_name='Descripción')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Precio')
    isbn = models.CharField(max_length=13, blank=True, verbose_name='ISBN')
    publication_date = models.DateField(blank=True, null=True, verbose_name='Fecha de publicación')
    pages = models.PositiveIntegerField(blank=True, null=True, verbose_name='Páginas')
    cover = models.ImageField(upload_to='book_covers/', blank=True, verbose_name='Portada')
    available = models.BooleanField(default=True, verbose_name='Disponible')
    featured = models.BooleanField(default=False, verbose_name='Destacado')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')
    updated = models.DateTimeField(auto_now=True, verbose_name='Fecha de actualización')
    
    class Meta:
        verbose_name = 'Libro'
        verbose_name_plural = 'Libros'
        ordering = ['-created']
    
    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('book_detail', args=[self.slug])
