from django.shortcuts import render

# Django
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from users.forms import ProfileForm, SignupForm
from django.views.generic import DetailView
from django.contrib.auth.models import User

from django.contrib.auth.views import LoginView, LogoutView


class UserLoginView(LoginView):
    """Login view"""
    template_name = "users/login.html"


# Sign in and sing up in one
def signup(request):
    if request.method == 'POST':
        if request.POST.get('email'):
            form = SignupForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('users:login')
    form = SignupForm()
    return render(
        request=request,
        template_name='users/login.html',
        context={'form': form}
    )


class UserLogOutView(LogoutView, LoginRequiredMixin):
    template_name = 'users/login.html'


@login_required
def update_profile(request):
    profile = request.user.profile
    if request.method == "POST":
        form = ProfileForm(request.POST, request.FILES)
        if form.is_valid():
            data = form.cleaned_data
            profile.biography = data['biography']
            profile.picture = data['picture']
            profile.save()
            return redirect('users:update_profile')
    else:
        form = ProfileForm()

    """ update a user's profile view """
    return render(
        request=request,
        template_name='users/update_profile.html',
        context={
            'profile': profile,
            'user': request.user,
            'form': form
        }
    )


class UserDetailView(DetailView, LoginRequiredMixin):
    template_name = 'user/detail.html'
    slug_field = "username"
    slug_url_kwarg = "username"  # Se tiene que llamar igual que en la url <str:slug_url_kwarg>
