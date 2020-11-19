# Django
from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, CreateView
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy

from libros.forms import BookForm, BookForm2, EditorialsForm, AuthoresForm
from libros.models import Books


@login_required
def home(request):
    books = Books.objects.all()
    return render(request, 'libros/home.html',
                  context={
                      'user': request.user,
                      'books': books
                  })


class EditorialCreateView(CreateView, LoginRequiredMixin):
    template_name = "libros/editorials/new.html"
    form_class = EditorialsForm
    success_url = reverse_lazy("libros:home")

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


class AuthoresCreateView(CreateView, LoginRequiredMixin):
    template_name = "libros/authores/new.html"
    form_class = AuthoresForm
    success_url = reverse_lazy("libros:home")

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)



@login_required
def new_book(request):
    if request.method == "POST":
        form = BookForm2(request.POST)
        if form.is_valid():
            form.save(request)
            return redirect('libros:home')
    else:
        form = BookForm2()
    return render(request=request,
                  template_name='libros/new_book.html',
                  context={
                      'form': form,
                      'user': request.user,
                      'profile': request.user.profile
                  }
                  )


@login_required
def delete(request):
    if request.method == "POST":
        Books.objects.filter(isbn=request.POST['delete_book']).delete()
        return render(request, "libros/home.html")
    redirect('libros:home')


class BookList(LoginRequiredMixin, ListView):
    model = Books

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['book_list'] = Books.objects.filter(user_id=self.request.user.id).order_by('-created')
        return context


#

class BookDetailView(DetailView, LoginRequiredMixin):
    template_name = "libros/<str:titulo>/detail.html"
    # queryset = Books.objects.filter(request.user.id)
    pass
