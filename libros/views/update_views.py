from django.views.generic import UpdateView
from libros.models import Books, Quotes
from django.urls import reverse_lazy
from libros.forms import QuotesForm
from django.shortcuts import render, redirect

""" Update views for quotes and revires showing detail books """


class LibroUpdateView(UpdateView):
    model = Books
    context_object_name = 'book'
    queryset = Books.objects.all()
    slug_field = 'isbn'
    slug_url_kwarg = 'isbn'
    template_name = "libros/books/detail.html"
    fields = [
        "description",
        "review",
    ]

    def post(self, request, **kwargs):
        self.object = self.get_object()
        if 'isbn' in request.POST:
            isbn = request.POST['isbn']
        else:
            isbn = self.get_context_data()['book'].isbn
        form_quote = QuotesForm(request.POST)
        if form_quote.is_valid():
            print("Es invalido")
            form_quote.instance.book = Books.objects.get(isbn=isbn)
            form_quote.save()

        return super().post(request, **kwargs)

    def get_success_url(self):
        isbn = self.get_context_data()['book'].isbn
        return reverse_lazy('libros:detail', kwargs={'isbn': isbn})
#

