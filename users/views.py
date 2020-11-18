from django.shortcuts import render

# Django
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from users.forms import ProfileForm, SignupForm
from django.views.generic import DetailView
from django.contrib.auth.models import User


# Models

# Sign in and sing up in one
def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        # Quiere decir que es un sign-up
        if request.POST.get('email'):
            form = SignupForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('users:login')
        else:
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                # Home es el nombre de nuestra url
                return redirect('libros:home')
            else:
                return render(request,
                              'users/login.html',
                              {'error': 'Invalid username or password'})
    form = SignupForm()
    return render(
        request=request,
        template_name='users/login.html',
        context={'form': form}
    )


# def signup(request):
#     if request.method == "POST":


@login_required
def logout_view(request):
    logout(request)
    return redirect('users:login')


@login_required
def update_profile(request):
    profile = request.user.profile
    if request.method == "POST":
        form = ProfileForm(request.POST, request.FILES)
        if form.is_valid():
            print(form.cleaned_data)
            data = form.cleaned_data
            profile.biography = data['biography']
            profile.picture = data['picture']
            profile.save()
            return redirect('users:update_profile')
            # para evitar que sea reenviado el formulario, tenemos que redireccionar
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
