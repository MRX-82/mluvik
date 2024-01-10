from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import User, Mluvi
from .forms import UserForm, Registration, AddWord
from .logika import verifications, added_word, word_learning


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
            return redirect(f"../{user_id}/set_mluvik")
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
    word_learn = word_learning(user_id)
    return render(request, "mluvik.html", {"user_name": id.login, "word_learn": word_learn})


def add_word(request, user_id):
    """
    Page of the adding word to application Mluvik
    """
    id = User.objects.get(id=user_id)
    user_id = id.id
    if request.method == "POST":
        new_word = request.POST.get('new_word')
        my_word = request.POST.get('my_word')
        word = added_word(my_word, new_word, user_id)
        return redirect(f"../../{user_id}/add_word")
    else:
        user_form = AddWord()
        return render(request, "add_word.html", {"user_name": id.login, "user_id": user_id,
                                                 "form": user_form})
