from .models import Book
from .serializers import BookSerializer
from rest_framework import viewsets
from django_filters import rest_framework as filters

from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter


class BookFilter(filters.FilterSet):

    class Meta:
        model = Book
        fields = {
            'title': ['icontains'],
            'authors': ['icontains'],
            'language': ['icontains'],
            'published_date': ['icontains'],
        }


class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    filter_class = BookFilter
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    ordering_fields = ['published_date']
