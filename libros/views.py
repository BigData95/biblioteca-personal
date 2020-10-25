# Django
from django.shortcuts import render
from django.http import HttpResponse

from django.contrib.auth.decorators import login_required

# Utilities


# Create your views here.
def index(request):
    return render(request, 'libros/index.html')

@login_required
def home(request):
    return render(request, 'libros/home.html')
