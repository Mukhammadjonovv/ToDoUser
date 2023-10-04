from django.shortcuts import render, redirect
from .models import *
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User

def index(request):
    if request.user.is_authenticated:
        content = {
            'todos': ToDo.objects.filter(owner=request.user)
        }
        return render(request, 'index.html', content)
    return redirect('/')
def edit(request):
    return render(request, 'edit.html')
def login_view(request):
    if request.method == 'POST':
        user = authenticate(
            username = request.POST.get("login"),
            password =request.POST.get("parol"),
        )  # None yoki topilgan userni return qiladi
        if user is None:
            return redirect('/')
        login(request, user)
        return redirect("/index/")
    return render(request, 'login.html')

def logout_view(request):
    logout(request)
    return redirect('/')
