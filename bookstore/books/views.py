from django.shortcuts import render, get_object_or_404
from .models import Author, Book

def authors_list(request):
    authors = Author.objects.all()
    return render(request, 'books/authors_list.html', {'authors': authors})

def author_detail(request, author_id):
    author = get_object_or_404(Author, id=author_id)
    books = author.books.all().order_by('publication_date')
    return render(request, 'books/author_detail.html', {'author': author, 'books': books})

def books_list(request):
    books = Book.objects.select_related('author', 'genre').all()
    return render(request, 'books/books_list.html', {'books': books})
