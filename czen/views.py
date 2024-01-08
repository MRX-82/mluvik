from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import User, Mluvi
from .forms import UserForm, Registration


def index(request):
    """
    Home page
    """
    return render(request, "index.html")


def registration_form(request):
    """
    This is function for registration new users
    """
    if request.method == "POST":
        login = request.POST.get('login')
        password = request.POST.get('password')
        my_language = request.POST.get('my_language')
        new_language = request.POST.get('new_language')
        registration_info = User.objects.create(
            login=login, password=password, my_language=my_language,
        new_language=new_language)
        registration_info.save()
        return HttpResponse(f"list{login}{password}{my_language}{new_language}")
    else:
        user_form = UserForm()
        return render(request, "registration_form.html", {"form": user_form})
