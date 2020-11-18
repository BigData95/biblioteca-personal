from django.urls import path
from users import views
# from users.views import *

urlpatterns = [
    path(route='users/login', view=views.login_view, name="login"),
    # <form method="POST" action="{% url "login" %}"> </form>  Se usa el nombre del url
    path(route='users/logout', view=views.logout_view, name="logout"),
    path(route='users/me/profile', view=views.update_profile, name='update_profile'),
    path(route="libros/detail/<str:username>",
         view=views.UserDetailView.as_view(),
         name="datail"
         )
]
