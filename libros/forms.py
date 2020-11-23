# Django
from django import forms
# Models
from libros.models import Books, Author, Editorials


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
                  # 'quotes',
                  # 'reviews',
                  # 'quotes'
                  }

    # def save(self):
    #     instance = forms.ModelForm.save(self)
    #     Author.books.add(BookForm)
    #     return instance
    #


# class BookForm2(forms.Form):
#     isbn = forms.IntegerField()
#     titulo = forms.CharField(min_length="1", max_length="50")
#     author = forms.ModelChoiceField(queryset=Author.objects.all(), required=False)
#     edicion = forms.IntegerField(required=False)
#     editorial = forms.ModelChoiceField(queryset=Editorials.objects.all(), required=False)
#     genre = forms.ChoiceField(choices=GENRE)
#     category = forms.ChoiceField(choices=CATEGORY)
#     year_of_publication = forms.IntegerField(required=False)
#     status = forms.ChoiceField(choices=STATUS)
#     portada = forms.ImageField(required=False)
#
#     def clean_book(self):
#         isbn = self.cleaned_data['isbn']
#         already_on_library = Books.objects.filter(isbn=isbn).exist()
#         if already_on_library:
#             raise ValidationError("Book already on library")
#         return isbn
#
#     def save(self, request):
#         data = self.cleaned_data
#         print(data)
#         book = Books.objects.create(user_id=request.user.pk,
#                                     profile_id=request.user.profile.pk,
#                                     **data
#                                     # isbn=data['isbn'],
#                                     # titulo=data['titulo'],
#                                     # portada=data['portada']
#
#                                     )
#         book.save()
