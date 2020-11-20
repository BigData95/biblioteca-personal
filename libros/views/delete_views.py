from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from libros.models import Books


@login_required
def delete(request):
    if request.method == "POST":
        Books.objects.filter(isbn=request.POST['delete_book']).delete()
        return render(request, "libros/home.html")
    redirect('libros:home')

