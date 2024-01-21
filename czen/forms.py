from django import forms
from .models import User
from django.forms import ModelForm


class UserForm(forms.Form):
    login = forms.CharField(max_length=20)
    password = forms.CharField(widget=forms.PasswordInput, max_length=20)


class Registration(forms.Form):
    login = forms.CharField(max_length=20)
    password = forms.CharField(max_length=20)
    my_language = forms.CharField(max_length=20)
    new_language = forms.CharField(max_length=20)


class AddWord(forms.Form):
    my_word = forms.CharField(max_length=20)
    new_word = forms.CharField(max_length=20)


class EnterTranslate(forms.Form):
    translate_word = forms.CharField(max_length=20)