from django.views.generic import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from libros.forms import EditorialsForm, AuthoresForm, BookForm
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy


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


class BooksCreateView(CreateView, LoginRequiredMixin):
    template_name = 'libros/books/new_book.html'
    form_class = BookForm
    success_url = reverse_lazy("libros:home")

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.instance.profile = self.request.user.profile
        form.save()
        return super().form_valid(form)


# @login_required
# def new_book(request):
#     if request.method == "POST":
#         form = BookForm2(request.POST)
#         if form.is_valid():
#             form.save(request)
#             return redirect('libros:home')
#     else:
#         form = BookForm2()
#     return render(request=request,
#                   template_name='libros/new_book.html',
#                   context={
#                       'form': form,
#                       'user': request.user,
#                       'profile': request.user.profile
#                   }
#                   )
