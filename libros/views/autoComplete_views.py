from dal import autocomplete
from django.utils.html import format_html

from libros.models import Author


class AuthorAutoComplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        if not self.request.user.is_authenticated:
            return Author.objects.none()
        queryset = Author.objects.all()
        if self.q:
            queryset = queryset.fileter(name__istartswith=self.q)
        return queryset

    # def get_resul_label(self, item):
    #     return item.name
