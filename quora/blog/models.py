from django.db import models
from django.contrib.auth.models import User


class Question(models.Model):
    author = models.ForeignKey("auth.User", on_delete=models.CASCADE)
    content = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    category = models.CharField(max_length=50, default='None')

    def __str__(self):
        return self.content


class Answer(models.Model):
    question = models.ForeignKey(
        Question, on_delete=models.CASCADE, related_name="answers")
    answer_author = models.CharField(max_length=50)
    answer_content = models.CharField(max_length=200)
    answer_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.answer_content
