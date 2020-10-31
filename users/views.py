from django.shortcuts import render

# Django
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from users.models import Profile


def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        # Quiere decir que es un sign-up
        if request.POST.get('email'):
            password_confirmation = request.POST['password_confirmation']
            if password != password_confirmation:
                return render(request, 'users/login.html',
                              {'error_create': 'Password does not match',
                               'anchor': 'signup'})
            else:
                user = User.objects.create_user(username='username', password=password)
                user.email = request.POST['email']
                profile = Profile(user=user)
                profile.save()
                return redirect('login')

        else:
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                # Home es el nombre de nuestra url
                return redirect('home')
            else:
                return render(request,
                              'users/login.html',
                              {'error': 'Invalid username or password'})
    return render(request, 'users/login.html')


@login_required
def logout_view(request):
    logout(request)
    return redirect('login')
