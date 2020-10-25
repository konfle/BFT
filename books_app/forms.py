from django import forms
from .models import Book
from django.forms import TextInput


class BookCreateForm(forms.ModelForm):

    class Meta:
        model = Book
        fields = ('title', 'authors', 'published_date', 'isbn_number', 'page_count', 'cover_link', 'language')
        widgets = {
            'title': TextInput(attrs={'class': 'form-control',
                                      'id': "title",
                                      'placeholder': "Enter Book Title"}),
            'authors': TextInput(attrs={'class': 'form-control',
                                        'id': "authors",
                                        'placeholder': "Enter Book Authors"}),
            'published_date': TextInput(attrs={'class': 'form-control',
                                               'id': "published_date",
                                               'placeholder': "Enter Book Published Date",
                                               'type': 'date'}),
            'isbn_number': TextInput(attrs={'class': 'form-control',
                                            'id': "isbn_number",
                                            'placeholder': "Enter Book ISBN Number"}),
            'page_count': TextInput(attrs={'class': 'form-control',
                                           'id': "page_count",
                                           'placeholder': "Enter Book Pages Count"}),
            'cover_link': TextInput(attrs={'class': 'form-control',
                                           'id': "cover_link",
                                           'placeholder': "Enter Book Cover Link"}),
            'language': TextInput(attrs={'class': 'form-control',
                                         'id': "language",
                                         'placeholder': "Enter Book Language"}),
        }
