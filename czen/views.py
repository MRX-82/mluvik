from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import User, Mluvi
from .forms import UserForm, Registration
from .logika import verifications


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
        user_form = Registration()
        return render(request, "registration_form.html", {"form": user_form})


def enter_mluvik(request):
    """
    This is function for enter autorizated users to Mluvik
    """
    if request.method == "POST":
        login = request.POST.get('login')
        password = request.POST.get('password')
        User_registr = User.objects.get(login=login)
        word_verifications = verifications(login, password, User_registr.login,
                                           User_registr.password)
        if word_verifications == "verification":
            user_id = User_registr.id
            return redirect(f"../set_mluvik/{user_id}")
        else:
            return HttpResponse(f"Password Error")
    else:
        user_form = UserForm()
        return render(request, "enter_mluvik.html", {"form": user_form})


def set_mluvik(request, user_id):
    """
    Starting set Mluvik applications
    """
    id = User.objects.get(id=user_id)
    user_id = id.id
    return render(request, "set_mluvik.html", {"user_name": id.login, "user_id": user_id})


def mluvik(request, user_id):
    """
    Home page applications
    """
    id = User.objects.get(id=user_id)
    user_id = id.id
    return render(request, "mluvik.html", {"user_name": id.login})


def add_word(request, user_id):
    """
    Page of the adding word to application Mluvik
    """
    id = User.objects.get(id=user_id)
    user_id = id.id
    return render(request, "add_word.html", {"user_name": id.login, "user_id": user_id})
