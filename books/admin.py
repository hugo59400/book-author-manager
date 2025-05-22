from django.contrib import admin
from .models import Author, Book, Genre

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'birth_date')
    search_fields = ('first_name', 'last_name')

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'genre', 'publication_date')
    search_fields = ('title', 'author__first_name', 'author__last_name')
    list_filter = ('genre',)

@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = ('name',)
