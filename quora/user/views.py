from django.shortcuts import render, HttpResponse, redirect, get_object_or_404
from .forms import RegisterForm, LoginForm
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from .models import Follow


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


def getUsers(request):
    users = User.objects.all()
    return render(request, "getUsers.html", {"users": users})


def follow(request, id):
    current_user = request.user
    user = User.objects.get(pk=id)
    print(current_user)
    current_user.following.add(Follow(following=user), bulk=False)
    return redirect('user:getUsers')
