# Django
from django.shortcuts import render, redirect
from django.http import HttpResponse

from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from libros.forms import BookForm
from libros.models import Books

# Utilities


# Create your views here.
def index(request):
    return render(request, 'libros/index.html')


@login_required
def home(request):
    books = Books.objects.all()
    print(books)
    return render(request, 'libros/home.html',
                  context={
                      'user': request.user,
                      'books': books
                  })


@login_required
def new_book(request):
    """Create new book """
    if request.method == "POST":
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = BookForm()
    return render(request=request,
                  template_name='libros/new_book.html',
                  context={
                      'form': form,
                      'user': request.user,
                      'profile': request.user.profile
                    }
                  )
