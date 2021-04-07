import django
from django.db import models
from django.urls import reverse
from django.utils import timezone


class Author(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)

    def __str__(self):
        return self.first_name, ' ', self.last_name


class Book(models.Model):
    title = models.CharField(max_length=50)
    authors = models.CharField(max_length=50)
    # authors = models.ForeignKey(Author, on_delete=models.CASCADE)
    published_date = models.DateTimeField()
    isbn_number = models.CharField(max_length=13)
    page_count = models.PositiveSmallIntegerField()
    cover_link = models.URLField()
    language = models.CharField(max_length=3)
    create_date = models.DateTimeField(default=django.utils.timezone.now)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('book_detail', kwargs={'pk': self.pk})
