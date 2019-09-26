from django.shortcuts import render, redirect, HttpResponse, get_object_or_404, reverse
from blog.models import Question, Answer
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
    authorized_user = [request.user.id]
    follower = request.user.following.all()
    for f in follower:
        authorized_user.append(f.following.id)
    questions = Question.objects.filter(
        category=category, author__in=authorized_user)
    return render(request, "singleCategory.html", {"questions": questions})


@login_required(login_url='/user/login/')
def getQuestion(request, id):
    questions = get_object_or_404(Question, id=id)
    answer = questions.answers.all()
    return render(request, "singleQuestion.html", {"questions": questions, "answers": answer})


@login_required(login_url='/user/login/')
def addAnswer(request, id):
    question = get_object_or_404(Question, id=id)
    if request.method == "POST":
        answer_author = request.user
        answer_content = request.POST.get("answer_content")

        newAnswer = Answer(answer_author=answer_author,
                           answer_content=answer_content)
        newAnswer.question = question
        newAnswer.save()
    return redirect(reverse("question:detail", kwargs={"id": id}))
