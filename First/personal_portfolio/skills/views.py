from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.db import IntegrityError
from .models import Skill

def index(request):
    skills = Skill.objects.all()
    return render(request, 'skills/index.html', {'skills': skills})

def signupuser(request):
    if request.method == 'GET':
        return render(request, 'skills/sign.html', {'form': UserCreationForm()})
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(
                    request.POST['username'],
                    password=request.POST['password1']
                )
                user.save()
                login(request, user)
                return redirect('current')
            except IntegrityError:
                return render(request, 'skills/sign.html', {'form': UserCreationForm(),
                                                          'error': 'Пользователь с таким именем уже существует!'})
        else:
            return render(request, 'skills/sign.html',
                          {'form': UserCreationForm(),
                           'error': 'Пароли не совпали!'})

def logoutuser(request):
    if request.method == 'POST':
        logout(request)
        return redirect('index')
    else:
        return render(request, 'skills/index.html')

def currenttodos(request):
    if request.user.is_authenticated:
        return render(request, 'skills/current.html')
    else:
        return redirect('index')

def loginuser(request):
    if request.method == 'GET':
        return render(request, 'skills/login.html', {'form': AuthenticationForm()})
    else:
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
            return render(request, 'skills/login.html',
                          {'form': AuthenticationForm(),
                           'error': 'Неверные данные для входа!'})
        else:
            login(request, user)
            return redirect('current')
