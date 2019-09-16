from django.shortcuts import render, redirect, HttpResponse
from blog.models import Question
from blog.forms import QuestionForm
from django.contrib import messages


def questions(request):
    questions = Question.objects.all().order_by('-created_date')
    return render(request, "question.html", {"questions": questions})


def addQuestion(request):
    form = QuestionForm(request.POST or None)
    if form.is_valid():
        question = form.save(commit=False)
        question.author = request.user
        question.save()
        messages.success(request, "Question asked")
        return redirect('question:dashboard')
    return render(request, "addQuestion.html", {"form": form})


def dashboard(request):
    questions = Question.objects.all()
    context = {
        "questions": questions
    }
    return render(request, "dashboard.html", context)
