from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import User, Mluvi


def imdex(request):
    """
    Home page
    """
    return render(request, "index.html")
