from rest_framework import serializers
from .models import Book


class BookSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Book
        fields = ('title', 'authors', 'published_date', 'isbn_number', 'page_count', 'cover_link', 'language')
