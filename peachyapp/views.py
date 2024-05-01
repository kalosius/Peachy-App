from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    return render(request, 'index.html', {})


def registration(request):
    return render(request, 'auth/register.html', {})

def user_login(request):
    return render(request, 'auth/login.html', {})