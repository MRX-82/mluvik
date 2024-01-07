from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import User, Mluvi


def index(request):
    """
    Home page
    """
    return render(request, "index.html")
