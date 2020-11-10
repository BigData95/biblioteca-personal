# Django
from django import forms

# Models
from libros.models import Books


class BookForm(forms.ModelForm):
    class Meta:
        """Form setting"""
        model = Books
        fields = ('user','profile', 'isbn', 'titulo', 'edicion')
