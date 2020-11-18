# Django
from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, CreateView
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy

from libros.forms import BookForm, BookForm2
from libros.models import Books


@login_required
def home(request):
    books = Books.objects.all()
    return render(request, 'libros/home.html',
                  context={
                      'user': request.user,
                      'books': books
                  })


# # CreateVIew most use a ModelForm (or something that exposes the exact same API as a ModelForm)
# class CreateNewBookView(CreateView, LoginRequiredMixin):
#     """Create new book"""
#     template_name = "libros/new_book.html"
#     form_class = BookForm2
#     success_url = reverse_lazy("libros:libros")
#
#     def get_context_data(self, **kwargs):
#         """Add user and profile to context"""
#         context = super().get_context_data(**kwargs)
#         context['user'] = self.request.user.id
#         context['profile'] = self.request.user.profile
#         return context
#
#     def form_valid(self, form):
#         form.save(self.request)
#         return super().form_valid(form)



@login_required
def new_book(request):
    if request.method == "POST":
        form = BookForm2(request.POST)
        if form.is_valid():
            # data = form.cleaned_data
            # libro = Books.objects.create(user_id=request.user.pk,
            #                  profile_id=request.user.profile.pk,
            #                  isbn=data['isbn'],
            #                  titulo=data['titulo'],
            #                  edicion=data['edicion']
            #                  )
            # data['profile.id'] = request.user.profile.pk
            # libro = Books.objects.create(isbn=data['isbn'],
            #                              titulo=data['titulo'],
            #                              edicion=['edicion'],
            #                              user=user,
            #                              profile=request.user.profile.pk
            #                              )
            # libro['isbn'] = data['isbn']
            # libro['titulo'] = data['titulo']
            # libro['edicion'] = data['edicion']
            # libro.save()
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
