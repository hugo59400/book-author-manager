
from django.db import models

class Genre(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    birth_date = models.DateField()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Book(models.Model):
    title = models.CharField(max_length=200)
    page_count = models.IntegerField()
    genre = models.ForeignKey(Genre, on_delete=models.SET_NULL, null=True)
    publication_date = models.DateField()
    cover_image = models.ImageField(upload_to='covers/', blank=True, null=True)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='books')

    def __str__(self):
        return self.title
