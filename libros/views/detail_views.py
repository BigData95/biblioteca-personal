from django.views.generic import DetailView
from libros.models import Author
from django.contrib.auth.mixins import LoginRequiredMixin


class BookDetailView(DetailView, LoginRequiredMixin):
    template_name = "libros/<str:titulo>/detail.html"
    # queryset = Books.objects.filter(request.user.id)
    pass


class AuthoreseDetailView(DetailView, LoginRequiredMixin):
    model = Author
    template_name = "libros/authores/detail.html"
