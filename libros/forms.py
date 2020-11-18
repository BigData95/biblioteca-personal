# Django
from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
# Models

from libros.models import Books
from users.models import Profile


class BookForm(forms.ModelForm):
    class Meta:
        """Form setting"""
        model = Books
        fields = ('user', 'profile', 'isbn', 'titulo', 'edicion')


class BookForm2(forms.Form):
    isbn = forms.IntegerField()
    titulo = forms.CharField(min_length="1", max_length="50")
    edicion = forms.IntegerField()

    def clean_book(self):
        isbn = self.cleaned_data['isbn']
        already_on_library = Books.objects.filter(isbn=isbn).exist()
        if already_on_library:
            raise ValidationError("Book already on library")
        return isbn

    def save(self, request):
        data = self.cleaned_data
        book = Books.objects.create(user_id=request.user.pk,
                                    profile_id=request.user.profile.pk,
                                    isbn=data['isbn'],
                                    titulo=data['titulo'],
                                    edicion=data['edicion']
                                    )
        book.save()
