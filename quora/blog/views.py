from django.shortcuts import render, redirect, HttpResponse
from blog.models import Question
from blog.forms import QuestionForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required


def homepage(request):
    return render(request, "homepage.html")


def categories(request):
    return render(request, "categories.html")


@login_required(login_url='/user/login/')
def dashboard(request):
    questions = Question.objects.all().order_by('-created_date')
    return render(request, "dashboard.html", {"questions": questions})


@login_required(login_url='/user/login/')
def addQuestion(request):
    form = QuestionForm(request.POST or None)
    if form.is_valid():
        question = form.save(commit=False)
        question.author = request.user
        question.save()
        messages.success(request, "Question asked")
        return redirect('question:dashboard')
    return render(request, "addQuestion.html", {"form": form})


@login_required(login_url='/user/login/')
def getSingleCategory(request, category):
    questions = Question.objects.filter(category=category)
    return render(request, "singleCategory.html", {"questions": questions})
