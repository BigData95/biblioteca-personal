# Django
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from libros.models import Books, Author


@login_required
def home(request):
    books = Books.objects.all()
    return render(request, 'libros/home.html',
                  context={
                      'user': request.user,
                      'books': books
                  })

