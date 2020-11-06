from django import forms


class ProfileForm(forms.Form):
    biography = forms.CharField(max_length=500, required=False)
    picture = forms.ImageField()
