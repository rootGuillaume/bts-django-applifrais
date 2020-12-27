from django.core.exceptions import ValidationError
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from django import forms
from .models import *


# Class || Form to create a new User
class UserCreationForm(forms.ModelForm):
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Password confirmation', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username', 'nom', 'prenom', 'adresse', 'cp', 'ville', 'dateEmbauche')

    # Function || Check that the two password entries match
    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise ValidationError("Passwords don't match")
        return password2

    # Function || Save the provided password in hashed format
    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user


# Class || Form to update an existing User
class UserChangeForm(forms.ModelForm):

    password = ReadOnlyPasswordHashField()

    class Meta:
        model = User
        fields = ('email', 'nom', 'prenom', 'adresse', 'cp', 'ville', 'dateEmbauche')

    def clean_password(self):
        return self.initial["password"]
