# Django
from django import forms
# Models
from libros.models import Books, Author, Editorials, Quotes
from django.forms import formset_factory


class EditorialsForm(forms.ModelForm):
    class Meta:
        model = Editorials
        fields = {'name', 'country'}


class AuthoresForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = '__all__'


class BookForm(forms.ModelForm):
    portada = forms.ImageField()

    class Meta:
        model = Books
        fields = {'isbn',
                  'titulo',
                  'author',
                  'portada',
                  'edicion',
                  'editorial',
                  'year_of_publication',
                  'genre',
                  'category',
                  'status',

                  }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['portada'].required = False


class QuotesForm(forms.ModelForm):
    class Meta:
        model = Quotes
        fields = ('quote',)


class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = ('name',)

