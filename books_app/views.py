from django.db.models import Q
from django.shortcuts import render
from .models import Book
from .forms import BookCreateForm
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)


def book_list(request):
    context = {
        'books': Book.objects.all()
    }
    return render(request, 'books_app/index.html', context)


class BooksListView(ListView):
    model = Book
    template_name = 'books_app/index.html'
    context_object_name = 'books'
    ordering = ['-create_date']


class BookDetailView(DetailView):
    model = Book
    template_name = 'books_app/detail.html'
    context_object_name = 'book'


class BookCreateView(CreateView):
    model = Book
    context_object_name = 'book'
    # fields = ['title', 'authors', 'published_date', 'isbn_number', 'page_count', 'cover_link', 'language']
    form_class = BookCreateForm


class BookUpdateView(UpdateView):
    model = Book
    context_object_name = 'book'
    form_class = BookCreateForm


class BookDeleteView(DeleteView):
    model = Book
    context_object_name = 'book'
    success_url = '/'


class BookSearchResultsView(ListView):
    model = Book
    template_name = 'books_app/book_search.html'

    def get_queryset(self):
        query = self.request.GET.get('search')
        object_list = Book.objects.filter(
            Q(title__contains=query) |
            Q(authors__icontains=query) |
            Q(language__icontains=query) |
            Q(published_date__icontains=query)
        )
        return object_list
