from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView
from libros.models import Books, Author, Editorials


class BookList(LoginRequiredMixin, ListView):
    model = Books
    template_name = 'libros/books/books_list.html'
    context_object_name = 'book_list'
    ordering = '-created'

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['book_list'] = Books.objects.filter(user_id=self.request.user.id).order_by('-created')
    #     # autores = Books.objects.select_related().all().values('author')
    #     # print(autores)
    #     # author = Books.objects.get(isbn=300)
    #     # print(author.author.all())
    #     return context


class AuthoresList(LoginRequiredMixin, ListView):
    model = Author
    template_name = 'libros/authores/list.html'
    context_object_name = 'author_list'
    ordering = 'name'

class EditorialsList(ListView, LoginRequiredMixin):
    model = Editorials
    pass
