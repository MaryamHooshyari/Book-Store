from django.urls import path
from .views.search import SearchResultsView
from .views.book import BookList, BookDetail
from .views.author import AuthorList, AuthorDetail
from .views.category import CategoryList, CategoryDetail

# search
urlpatterns = [
    path('search/', SearchResultsView.as_view(), name='search_result')
]

# book
urlpatterns += [
    path('book/', BookList.as_view(), name='book_list'),
    path('book/<slug>', BookDetail.as_view(), name='book_detail'),
]

# author
urlpatterns += [
    path('author/', AuthorList.as_view(), name='author_list'),
    path('author/<slug>', AuthorDetail.as_view(), name='author_detail'),
]

# category
urlpatterns += [
    path('category/', CategoryList.as_view(), name='category_list'),
    path('category/<slug>', CategoryDetail.as_view(), name='category_detail'),
]
