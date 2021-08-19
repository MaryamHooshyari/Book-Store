from django.urls import path
from .views.search import SearchResultsView

urlpatterns = [
    path('search/', SearchResultsView.as_view(), name='search_result')
]
