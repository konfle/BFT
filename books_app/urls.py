from django.urls import path, include

from .router import router
from .views import (
    BooksListView,
    BookDetailView,
    BookCreateView,
    BookUpdateView,
    BookDeleteView,
    BookSearchResultsView,
)

urlpatterns = [
    path('', BooksListView.as_view(), name='book_list'),
    path('book/<int:pk>/', BookDetailView.as_view(), name='book_detail'),
    path('book/new/', BookCreateView.as_view(), name='book_create'),
    path('book/<int:pk>/update/', BookUpdateView.as_view(), name='book_update'),
    path('book/<int:pk>/delete/', BookDeleteView.as_view(), name='book_delete'),
    path('book/', BookSearchResultsView.as_view(), name='book_search'),
    # API URL
    path('api/', include(router.urls))
]
