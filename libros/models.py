from django.db import models

from django.contrib.auth.models import User

GENDER = [('Meele', 'Dude'), ('Feemele', 'Woman')]


class Author(models.Model):
    name = models.CharField(max_length=50)
    gender = models.CharField(max_length=7,  choices=GENDER)
    birth_date = models.DateField(blank=True, null=True)

    def __str__(self):
        return self.name


class Books(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    profile = models.ForeignKey('users.Profile', on_delete=models.CASCADE)
    # authors = models.ManyToManyField(Author)
    isbn = models.IntegerField(unique=True, primary_key=True, blank=False)
    titulo = models.CharField(max_length=50, blank=False)
    # Autor = models.ForeignKey()
    edicion = models.IntegerField(blank=True)

    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    # review = Foreanea
    # Citas foreanea
    # Categoria, foranea
    # status = Custom field

    def __str__(self):
        return f"Titulo: {self.titulo}"
