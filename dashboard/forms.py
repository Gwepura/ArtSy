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

class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ['question_text']
        labels = {
            'question_text': 'Question',
        }
        widgets = {
            'question_text': forms.TextInput(attrs={'class': 'form-control'}),
        }

class ResponseForm(forms.ModelForm):
    class Meta:
        model = Response
        fields = ['response']
        labels = {
            'response': 'Response',
        }
        widgets = {
            'response': forms.TextInput(attrs={'class': 'form-control'}),
        }

class TeamMemberForm(forms.ModelForm):
    class Meta:
        model = TeamMember
        fields = ['name', 'designation', 'bio', 'icon', 'position', 'active']
        labels = {
            'name': 'Name',
            'designation': 'Designation',
            'bio': 'Bio',
            'icon': 'Icon',
            'position': 'Position',
            'active': 'Active',
        }
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'designation': forms.TextInput(attrs={'class': 'form-control'}),
            'bio': forms.Textarea(attrs={'class': 'form-control'}),
            'icon': forms.TextInput(attrs={'class': 'form-control'}),
            'position': forms.NumberInput(attrs={'class': 'form-control'}),
            'active': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }