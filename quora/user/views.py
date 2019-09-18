from django.shortcuts import render, HttpResponse, redirect
from .forms import RegisterForm, LoginForm
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages


def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')

            newUser = User(username=username)
            newUser.set_password(password)
            newUser.save()
            login(request, newUser)
            messages.success(request, 'Basari ile kayit oldunuz')
            return render(request, "homepage.html")
        context = {
            "form": form
        }
        return render(request, 'register.html', context)
    else:
        form = RegisterForm()
        context = {
            "form": form
        }
        return render(request, 'register.html', context)


def loginUser(request):
    form = LoginForm(request.POST or None)
    context = {
        "form": form
    }
    if form.is_valid():
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        user = authenticate(username=username, password=password)

        if user is None:
            messages.info(request, 'Kullanici adi veya parola hatali')
            return render(request, "login.html", context)
        messages.success(request, 'Basari ile giris yaptiniz.')
        login(request, user)
        return redirect('question:dashboard')
    return render(request, 'login.html', context)


def logoutUser(request):
    logout(request)
    return redirect('home')
