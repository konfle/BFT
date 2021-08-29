from django.urls import path, include

from .router import router
from .views import (
    BooksListView,
    BookDetailView,
    BookCreateView,
    BookUpdateView,
    BookDeleteView,
    BookSearchResultsView,
    search_import,
    get_book_from_api,
)

urlpatterns = [
    path('', BooksListView.as_view(), name='book_list'),
    path('book/<int:pk>/', BookDetailView.as_view(), name='book_detail'),
    path('book/new/', BookCreateView.as_view(), name='book_create'),
    path('book/<int:pk>/update/', BookUpdateView.as_view(), name='book_update'),
    path('book/<int:pk>/delete/', BookDeleteView.as_view(), name='book_delete'),
    path('book/', BookSearchResultsView.as_view(), name='book_search'),
    # path('book/import/search/', BookSearchImportView.as_view(), name='search_import'),
    path('book/import/search/', search_import, name='search_import'),
    path('book/import/', get_book_from_api, name='get_book'),
    # API URL
    path('api/', include(router.urls))
]
