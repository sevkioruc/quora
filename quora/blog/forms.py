from django import forms
from blog.models import Question


class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ["content"]
