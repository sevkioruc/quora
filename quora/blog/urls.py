
from django.contrib import admin
from django.urls import path
from blog import views

app_name = "question"

urlpatterns = [
    path('', views.questions, name="questions"),
    path('add/', views.addQuestion, name="addquestion"),
    path('dashboard/', views.dashboard, name="dashboard"),
    path('home/', views.homepage, name="home")
]
