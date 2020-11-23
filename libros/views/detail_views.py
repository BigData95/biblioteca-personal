from django.shortcuts import get_object_or_404
from django.views.generic import DetailView
from libros.models import Author, Books
from libros.views.update_views import LibroUpdateView
from django.contrib.auth.mixins import LoginRequiredMixin


class BookDetailView(DetailView, LoginRequiredMixin):
    model = Books
    template_name = "libros/books/detail.html"
    queryset = Books.objects.all()
    slug_field = 'isbn'
    slug_url_kwarg = 'isbn'
    context_object_name = "book"


class AuthoreseDetailView(DetailView, LoginRequiredMixin):
    model = Author
    template_name = "libros/authores/detail.html"
