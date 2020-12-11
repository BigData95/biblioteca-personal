"""Libros Url"""
from django.conf.urls.static import static
from django.urls import path, re_path
from django.conf.urls import url
from dal import autocomplete
from libros.models import Author

from Biblioteca import settings
from django.views.generic import TemplateView
from libros.views import (
    create_views,
    delete_views,
    detail_views,
    general,
    listing_views,
    update_views,
    autoComplete_views
)

urlpatterns = [
    path('index/',
         TemplateView.as_view(template_name='libros/index.html'),
         name="index"
         ),
    path(route='home/',
         view=general.home,
         name="home"
         ),
    path(route="books/new",
         view=create_views.BooksCreateView.as_view(),
         name="new_book"
         ),
    path(route="books/editorials/new",
         view=create_views.EditorialCreateView.as_view(),
         name="new_editorial"
         ),
    path(route="books/authores/new",
         view=create_views.AuthoresCreateView.as_view(),
         name="new_author"
         ),
    path(route="books/delete",
         view=delete_views.delete,
         name="delete"
         ),
    path(route='quote/delete',
         view=delete_views.delete_quote,
         name='delete_quote'
         ),
    path(route="books/authores/authores",
         view=listing_views.AuthoresList.as_view(),
         name="authores"

         ),
    path(route="books/<str:username>/",
         view=listing_views.BookList.as_view(),
         name="libros"
         ),
    path(route="books/detail/<int:isbn>",
         view=update_views.LibroUpdateView.as_view(),
         name="detail"
         ),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
