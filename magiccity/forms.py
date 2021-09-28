from magiccity.models import Business, Neighbourhood, Profile, Post
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class SignupForm(UserCreationForm):
    email = forms.EmailField(max_length=250)

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['user', 'id_number', 'bio']

