from django.conf.urls.static import static
from django.urls import path

from Biblioteca import settings
from users import views
# from users.views import *

urlpatterns = [
    path(route='users/signup', view=views.signup, name="signup"),
    path(route="users/login", view=views.UserLoginView.as_view(), name="login"),
    path(route="users/logout", view=views.UserLogOutView.as_view(), name="logout"),

    path(route='users/me/profile', view=views.update_profile, name='update_profile'),
    path(route="libros/detail/<str:username>",
         view=views.UserDetailView.as_view(),
         name="datail"
         )
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
