from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import User, Mluvi
from .forms import UserForm, Registration, AddWord, EnterTranslate
from .logika import verifications, added_word, word_learning, word_status, word_repetition_check


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
    words_learn = word_learning(user_id)
    if request.method == "POST":
        translate_word = request.POST.get('translate_word')
        if words_learn[0][1] == translate_word:
            oks = word_status(user_id, translate_word)
            return redirect(f"../../{user_id}/mluvik")
        else:
            return HttpResponse(f"ERRRORR")
    else:
        form = EnterTranslate()
        return render(request, "mluvik.html", {"user_name": id.login,
                                               "word_learn": words_learn[0][0],
                                               "form": form})


def add_word(request, user_id):
    """
    Page of the adding word to application Mluvik
    """
    id = User.objects.get(id=user_id)
    user_id = id.id
    my_language = id.my_language
    new_language = id.new_language
    if request.method == "POST":
        new_word = request.POST.get('new_word')
        my_word = request.POST.get('my_word')
        check_word = word_repetition_check(user_id, my_word)
        if check_word == "No":
            word = added_word(my_word, new_word, user_id)
            return redirect(f"../../{user_id}/add_word")
        else:
            return HttpResponse(f"This word database is have")
    else:
        user_form = AddWord()
        return render(request, "add_word.html", {"user_name": id.login, "user_id": user_id,
            "form": user_form, "my_language": my_language, "new_language": new_language})
