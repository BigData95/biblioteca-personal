from django.db import models
from django.contrib.auth.models import User
from libros.fields import CountryField

GENRE = [
    ('Fantasy', 'Fantasy'),
    ('Sci-Fi', 'Sci-Fi'),
    ('Romance', 'Romance'),
    ('Horror', 'Horror'),
    ('Drama', 'Drama'),
    ('Classic', 'Classic'),
    ('Other', 'Other')
]
CATEGORY = [
    ('Novel', 'Novel'),
    ('Poetry', 'Poetry'),
    ('Stories', 'Stories'),
    ('Biography', 'Biography'),
    ('Philosophy', 'Philosophy'),
    ('Math', 'Math'),
    ('Complete Work', 'Complete Work'),
    ('History', 'History'),
    ('Dictionary', 'Dictionary'),
    ('Art/architecture', 'Art/architecture'),
    ('Science', 'Science'),
    ('Other', 'Other')
]

STATUS = [
    ('readed', 'readed'),
    ('to read', 'to read'),
    ('reading', 'reading')
]


class Editorials(models.Model):
    name = models.CharField(unique=True, max_length=50)
    country = CountryField(default='UN')

    def __str__(self):
        return self.name


class Books(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # OneToMany ralation
    profile = models.ForeignKey('users.Profile', on_delete=models.CASCADE)

    isbn = models.IntegerField(unique=True, primary_key=True, blank=False)
    titulo = models.CharField(max_length=50, blank=False)
    portada = models.ImageField(upload_to="books/", blank=True)
    # author = models.ManyToManyField('Author')   # Solo una tabla es necesaria que tenga esta relacion
    edicion = models.IntegerField(blank=True)

    editorial = models.ForeignKey(Editorials, on_delete=models.CASCADE, blank=True)
    year_of_publication = models.IntegerField(blank=True)

    # quotes = models.ManyToManyField('Quotes', on_delete=models.CASCADE)
    genre = models.CharField(choices=CATEGORY, default='Other', max_length=20)
    category = models.CharField(choices=CATEGORY, default='Novel', max_length=20)
    # reviews = models.ManyToManyField('Reviews', on_delete=models.CASCADE)
    status = models.CharField(choices=STATUS, default='to read', max_length=20)

    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Titulo: {self.titulo}"


class Author(models.Model):
    # First elemnt is the actual value to be stored and second is the human-readble name
    GENDER = [('Meele', 'Man'), ('Feemele', 'Woman')]
    name = models.CharField(unique=True, max_length=50)
    picture = models.ImageField(upload_to="authores/", blank=True)
    country = CountryField(default='UN')
    books = models.ManyToManyField(Books, blank=True)
    biography = models.TextField(blank=True)
    gender = models.CharField(max_length=7, choices=GENDER)
    birth_date = models.DateField(blank=True, null=True)

    def __str__(self):
        return self.name


class Reviews(models.Model):
    Book = models.ManyToManyField(Books, blank=True)
    Author = models.ForeignKey(User, on_delete=models.CASCADE)
    review = models.TextField()


class Quotes(models.Model):
    Book = models.ManyToManyField(Books, blank=True)
    Author = models.ForeignKey(User, on_delete=models.CASCADE)
    quote = models.TextField()
