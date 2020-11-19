# Django
from django import forms
from django.contrib.auth.models import User
from libros.models import Author, Editorials
from django.core.exceptions import ValidationError
# Models

from libros.models import Books, GENRE, CATEGORY, STATUS
from users.models import Profile


class EditorialsForm(forms.ModelForm):
    class Meta:
        model = Editorials
        fields = {'name', 'country'}


class AuthoresForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = '__all__'
        # fields = {'name', 'country', 'biography', 'gender', 'birth_date'}


class BookForm(forms.ModelForm):
    class Meta:
        """Form setting"""
        model = Books
        fields = ('user', 'profile', 'isbn', 'titulo', 'edicion')


class BookForm2(forms.Form):
    isbn = forms.IntegerField()
    titulo = forms.CharField(min_length="1", max_length="50")
    author = forms.ModelChoiceField(queryset=Author.objects.all(), widget=forms.CheckboxSelectMultiple, required=False)
    edicion = forms.IntegerField(required=False)
    editorial = forms.ModelChoiceField(queryset=Editorials.objects.all(), required=False)
    year_of_publication = forms.IntegerField(required=False)
    genre = forms.ChoiceField(choices=GENRE)
    category = forms.ChoiceField(choices=CATEGORY)
    status = forms.ChoiceField(choices=STATUS)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # context['Authores'] = Author.objects.all()
        # context['Category'] =
        return context

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
