"""Libros Url"""
from django.urls import path
from libros import views
from django.views.generic import TemplateView

urlpatterns = [
    path('index/',
         TemplateView.as_view(template_name='libros/index.html'),
         name="index"
         ),
    path(route='home/',
         view=views.home,
         name="home"
         ),
    path(route='books/new',
         view=views.new_book,
         name="new_book"
         ),
    path(route="home",
         view=views.delete,
         name="delete"
         ),
    path(route="libros/<str:username>/",
         view=views.BookList.as_view(),
         name="libros"),
]
