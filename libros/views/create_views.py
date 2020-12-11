from django.shortcuts import render
from django.views.generic import CreateView
from django.forms import inlineformset_factory
from django.contrib.auth.mixins import LoginRequiredMixin
from libros.forms import EditorialsForm, AuthoresForm, BookForm
from django.urls import reverse_lazy
from libros.models import Books, Author


class EditorialCreateView(CreateView, LoginRequiredMixin):
    template_name = "libros/editorials/new.html"
    form_class = EditorialsForm
    success_url = reverse_lazy("libros:home")

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


class AuthoresCreateView(CreateView, LoginRequiredMixin):
    template_name = "libros/authores/new.html"
    form_class = AuthoresForm
    success_url = reverse_lazy("libros:home")


class BooksCreateView(CreateView, LoginRequiredMixin):
    template_name = 'libros/books/new_book.html'
    form_class = BookForm
    success_url = reverse_lazy("libros:home")

    # def get_context_data(self, **kwargs):
    #     contexto = super().get_context_data(**kwargs)
    #     if self.request.POST:
    #         contexto['authorForm'] = AuthoresForm(self.request.POST)
    #     else:
    #         contexto['authorForm'] = AuthoresForm()
    #     return contexto

    def form_valid(self, form):
        # Se tiene que agregar los datos del usuario y el perfil
        form.instance.user = self.request.user
        form.instance.profile = self.request.user.profile
        form.save()
        return super().form_valid(form)
