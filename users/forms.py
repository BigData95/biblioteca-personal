from django import forms
from django.contrib.auth.models import User
from users.models import Profile


class ProfileForm(forms.Form):
    biography = forms.CharField(max_length=500, required=False)
    picture = forms.ImageField()


class SignupForm(forms.Form):
    username = forms.CharField(min_length=4, max_length=15)
    email = forms.EmailField(min_length=6, max_length=30)
    # email = forms.CharField(min_length=6, max_length=30, widget=forms.EmailInput())
    password = forms.CharField(max_length=30, widget=forms.PasswordInput())
    password_confirmation = forms.CharField(max_length=30, widget=forms.PasswordInput())

    def clean_username(self):
        """Username must be unique"""
        username = self.cleaned_data['username']
        # Si usamos .get y estaba vacia lanza una excepcion
        username_taken = User.objects.filter(username=username).exists()  # Regresa Booloeano
        if username_taken:
            raise forms.ValidationError("Username is already in use.")
        return username

    def clean(self):
        """Verify password confirmation match"""
        data = super().clean()
        password = data['password']
        password_confirmation = data['password_confirmation']
        if password != password_confirmation:
            raise forms.ValidationError("Passwords do not match")
        return data

    def save(self):
        data = self.cleaned_data
        data.pop('password_confirmation')
        user = User.objects.create_user(**data)
        profile = Profile(user=user)
        profile.save()
