from django import forms
from . models import Student
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class studentForm(forms.ModelForm):
    class Meta:
        model=Student
        fields=['firstName','secondName','age']

class customUser(UserCreationForm):
    class Meta:
        model=User
        fields=['username','password1','password2']