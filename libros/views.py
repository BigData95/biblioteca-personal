# Django
from django.shortcuts import render, redirect
from django.views.generic import DetailView, TemplateView, ListView
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

from libros.forms import BookForm, BookForm2
from libros.models import Books


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
    """Create new book !FOR ALL USERS"""
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


class BookList(LoginRequiredMixin, ListView):
    model = Books
    ordering = ('-created',)
    context_object_name = 'book_list'

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['book_list'] = Books.objects.all()
    #     return context

    # template_view = 'libros/libros.html'
    # slug_field = 'username'
    # slug_url_kwarg = 'username'  # EL nombre que le pusimos en las urls
    # queryset = User.objects.all()
    # context_object_name = 'user'
    #
    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     user = self.get_object()
    #     context['books'] = Books.objects.filter(user=user).order_by('-created')
    #     return context


#
# class UserDatailView(TemplateView):

def delete(request):
    if request.method == "POST":
        print(request.post)

    redirect('libros:home')
