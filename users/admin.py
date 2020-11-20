from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

# Models
from users.models import Profile
from libros.models import Books
from django.contrib.auth.models import User


# Register your models here.


# admin.site.register(Profile)

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('pk', 'user', 'picture')

    # list_editable = ()  Parametros que se pueden editar desde el admin
    search_fields = ('user__email', 'user__first_name')
    list_filter = ('created', 'modified', 'user__is_active', 'user__is_staff')


@admin.register(Books)
class BooksAdmin(admin.ModelAdmin):
    list_display = ('isbn', 'titulo')
    search_fields = ('isbn',)


class ProfileInline(admin.StackedInline):
    """ Profile in-line admin for users"""
    model = Profile
    can_delete = False
    verbose_name_plural = "profiles"


class BooksInline(admin.StackedInline):
    model = Books
    can_delete = False
    verbose_name = "libros"


class UserAdmin(BaseUserAdmin):
    """
    Add Profile admin to base user admin
    """
    inlines = (ProfileInline, BooksInline,)


admin.site.unregister(User)
admin.site.register(User, UserAdmin)
