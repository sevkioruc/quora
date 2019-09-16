from django import forms
from blog.models import Question


class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ["content", "category"]
        AGE_CHOICES = (
            ('', 'Select a category'),
            ('Science', 'Science'),
            ('Sport', 'Sport'),
            ('Technology', 'Technology'),
            ('Nature', 'Nature'),
            ('Social', 'Social'),
            ('Literature', 'Literature')
        )
        widgets = {
            'category': forms.Select(choices=AGE_CHOICES)
        }
