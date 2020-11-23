from django.views.generic import UpdateView
from libros.models import Books, Quotes
from django.urls import reverse_lazy

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
    success_url = reverse_lazy("libros:detail",
                               kwargs={'isbn': queryset.values('isbn').first()['isbn']})


    def post(self, request, **kwargs):
        isbn = self.queryset.values('isbn').first()['isbn']
        request.POST = request.POST.copy()
        if 'quote' in request.POST:
            book = Books.objects.get(isbn=isbn)
            quote = Quotes.objects.create(quote=request.POST['quote'], book=book)
            quote.save()

        return super().post(request, **kwargs)

#
# def detail_update_create(request):
#     if request.POST:
#         if 'create_quote' in request.POST:
#             print('Vamos a crear un quote')
#             pass
#         if 'update_review' in request.POST:
#             print('Vamos hacer update')
#             pass
#     else:
#         form1 = QuotesForm()
