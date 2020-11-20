from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView
from libros.models import Books, Author, Editorials


class BookList(LoginRequiredMixin, ListView):
    model = Books
    template_name = 'libros/books/books_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['book_list'] = Books.objects.filter(user_id=self.request.user.id).order_by('-created')
        return context


class AuthoresList(LoginRequiredMixin, ListView):
    model = Author
    pass


class EditorialsList(ListView, LoginRequiredMixin):
    model = Editorials
    pass
