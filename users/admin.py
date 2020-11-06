from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

# Models
from users.models import Profile
from django.contrib.auth.models import User


# Register your models here.


# admin.site.register(Profile)

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('pk', 'user', 'picture')
    # list_editable = ()  Parametros que se pueden editar desde el admin
    search_fields = ('user__email', 'user__first_name')
    list_filter = ('created', 'modified', 'user__is_active', 'user__is_staff')


class ProfileInline(admin.StackedInline):
    """ Profile in-line admin for users"""
    model = Profile
    can_delete = False
    verbose_name_plural = "profiles"


class UserAdmin(BaseUserAdmin):
    """
    Add Profile admin to base user admin
    """
    inlines = (ProfileInline,)


admin.site.unregister(User)
admin.site.register(User, UserAdmin)
