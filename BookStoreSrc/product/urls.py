from django.urls import path

from .views.author import (AuthorCreate, AuthorDelete, AuthorDetail,
                           AuthorList, AuthorUpdate, StaffAuthor,
                           StaffAuthorDetail)
# staff
from .views.book import (BookCreate, BookDelete, BookDetail, BookList,
                         BookUpdate)
from .views.category import (CategoryCreate, CategoryDelete, CategoryDetail,
                             CategoryList, CategoryUpdate, StaffCategory,
                             StaffCategoryDetail)
from .views.home import HomeView
from .views.search import SearchResultsView

# home
urlpatterns = [
    path('', HomeView.as_view(), name='home')
]

# search
urlpatterns += [
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

# staff
urlpatterns += [
    # book
    path('staff/book/create/', BookCreate.as_view(), name='book_create'),
    path('staff/book/edit/<int:pk>', BookUpdate.as_view(), name='book_edit'),
    path('staff/book/delete/<int:pk>', BookDelete.as_view(), name='book_delete'),

    # category
    path('staff/category/', StaffCategory.as_view(), name='staff_category'),
    path('staff/category/<slug>', StaffCategoryDetail.as_view(), name='staff_category_detail'),
    path('staff/category/create/', CategoryCreate.as_view(), name='category_create'),
    path('staff/category/edit/<int:pk>', CategoryUpdate.as_view(), name='category_edit'),
    path('staff/category/delete/<int:pk>', CategoryDelete.as_view(), name='category_delete'),

    # author
    path('staff/author/', StaffAuthor.as_view(), name='staff_author'),
    path('staff/author/<slug>', StaffAuthorDetail.as_view(), name='staff_author_detail'),
    path('staff/author/create/', AuthorCreate.as_view(), name='author_create'),
    path('staff/author/edit/<int:pk>', AuthorUpdate.as_view(), name='author_edit'),
    path('staff/author/delete/<int:pk>', AuthorDelete.as_view(), name='author_delete'),
]
