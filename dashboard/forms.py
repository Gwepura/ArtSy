from django import forms
from .models import *

class EmailForm(forms.ModelForm):
    class Meta:
        model = Email
        fields = ['email', 'name', 'subject', 'message']
        # fiels = '__all__'
        labels = {
            'email': 'Email',
            'name': 'Name',
            'subject': 'Subject',
            'message': 'Message',
        }
        widgets = {
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'subject': forms.TextInput(attrs={'class': 'form-control'}),
            'message': forms.Textarea(attrs={'class': 'form-control'}),
        }

class QuestionForm(forms.Form):
    class Meta:
        model = Question
        fields = ['question_text']
        labels = {
            'question_text': 'Question',
        }
        widgets = {
            'question_text': forms.TextInput(attrs={'class': 'form-control'}),
        }

class ResponseForm(forms.Form):
    class Meta:
        model = Response
        fields = ['response']
        labels = {
            'response': 'Response',
        }
        widgets = {
            'response': forms.TextInput(attrs={'class': 'form-control'}),
        }