from django.urls import path
from . import views

urlpatterns = [
    path('authors/', views.authors_list, name='authors_list'),
    path('authors/<int:author_id>/', views.author_detail, name='author_detail'),
    path('books/', views.books_list, name='books_list'),
    path('', views.home, name='home'),

]