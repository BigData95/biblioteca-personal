from django.shortcuts import render

# Django
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from users.forms import ProfileForm, SignupForm


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
            # password_confirmation = request.POST['password_confirmation']
            # if password != password_confirmation:
            #     return render(request, 'users/login.html',
            #                   {'error_create': 'Password does not match',
            #                    'anchor': 'signup'})
            # else:
            #     try:
            #         user = User.objects.create_user(username='username', password=password)
            #     except IntegrityError:
            #         return render(request, 'users/login.html',
            #                       {'error_create': 'Username is already in use',
            #                        'anchor': 'signup'})
            #     user.email = request.POST['email']
            #     user.save()
            #     profile = Profile(user=user)
            #     profile.save()
            #     return redirect('login')
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
