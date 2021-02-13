# Django
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from libros.models import Books, Author


from allauth.account.decorators import verified_email_required


@login_required
# @verified_email_required
def home(request):
    books = Books.objects.all()
    return render(request, 'libros/home.html',
                  context={
                      'user': request.user,
                      'books': books
                  })

