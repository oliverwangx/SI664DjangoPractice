from django.urls import path
from . import views
import os
from django.urls import re_path
from django.views.static import serve
from django.conf import settings
urlpatterns = [
    path('', views.index, name='index'),
    path('books/', views.BookListView.as_view(), name='books'),
    path('book/<int:pk>', views.BookDetailView.as_view(), name='book-detail'),
    path('authors/', views.AuthorListView.as_view(), name='authors'),
    path('author/<int:pk>',
         views.AuthorDetailView.as_view(), name='author-detail'),
]

# New lines below to serve static files in debug mode


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

urlpatterns += [
    re_path(r'^static/(?P<path>.*)$', serve, {
        'document_root': os.path.join(BASE_DIR, 'catalog/static'),
    }),
]

urlpatterns += [
    path('mybooks/', views.LoanedBooksByUserListView.as_view(), name='my-borrowed'),
]