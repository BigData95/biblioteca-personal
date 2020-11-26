from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required

from django.urls import reverse_lazy
from django.views.generic import DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from libros.models import Books, Quotes


@login_required
def delete(request):
    """Delete a book from the data base"""
    if request.method == "POST":
        Books.objects.get(isbn=request.POST['delete_book']).delete()
    return redirect('libros:home')


def delete_quote(request):
    isbn = None
    if request.method == "POST":
        _id = request.POST['delete_quote']
        Quotes.objects.get(id=_id).delete()
        isbn = request.POST['redirect']
    if isbn:
        return HttpResponseRedirect(reverse_lazy('libros:detail', kwargs={'isbn':isbn}))
    else:
        return redirect("libros:home")
