from django import forms
from models import User

class UserForm(forms.Form):
    login = forms.CharField(max_length=20)
    password = forms.CharField(max_length=20)


class Registrations(forms.Form):
    login = forms.CharField(max_length=20)
    password = forms.CharField(max_length=20)
    my_language = forms.CharField(max_length=20)
    new_language = forms.CharField(max_length=20)