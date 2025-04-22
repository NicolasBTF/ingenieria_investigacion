# books/admin.py

from django.contrib import admin
from .models import Category, Author, Book
from django.utils.safestring import mark_safe

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}
    search_fields = ['name']

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ['name']
    search_fields = ['name']
    fieldsets = (
        (None, {
            'fields': ('name', 'bio')
        }),
    )

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'price', 'available', 'featured', 'display_cover']
    list_filter = ['available', 'featured', 'created', 'author', 'categories']
    search_fields = ['title', 'description', 'isbn']
    prepopulated_fields = {'slug': ('title',)}
    date_hierarchy = 'created'
    raw_id_fields = ['author']
    filter_horizontal = ['categories']
    list_editable = ['price', 'available', 'featured']
    
    fieldsets = (
        ('Información básica', {
            'fields': ('title', 'slug', 'author', 'description', 'categories')
        }),
        ('Detalles', {
            'fields': ('price', 'isbn', 'publication_date', 'pages')
        }),
        ('Imagen', {
            'fields': ('cover',)
        }),
        ('Estado', {
            'fields': ('available', 'featured')
        }),
    )
    
    def display_cover(self, obj):
        if obj.cover:
            return mark_safe(f'<img src="{obj.cover.url}" width="50" height="70" />')
        return "Sin portada"
    display_cover.short_description = 'Portada'
