from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse

from .models import *
from .forms import *

# Create your views here.
def index(request):
    return render(request, 'dashboard/index.html')

def view_emails(request):
    return render(request, 'emails/index.html', {
        'emails': Email.objects.all()
    })

def view_email(request, id):
    email = Email.objects.get(id=id)

    return HttpResponseRedirect(reverse('view_emails'))

def add_email(request):
    if request.method == 'POST':
        form = EmailForm(request.POST)

        if form.is_valid():
            new_email = Email(
                email=form.cleaned_data['email'],
                name=form.cleaned_data['name'],
                subject=form.cleaned_data['subject'],
                message=form.cleaned_data['message']
            )

            new_email.save()

            return render(request, 'emails/index.html', {
                'form': EmailForm(),
                'success': True,
            })
    else:
        form = EmailForm()

    return render(request, 'emails/add.html', {
        'email': EmailForm()
    })
        
def edit_email(request, id):
    if request.method == 'POST':
        email = Email.objects.get(id=id)
        form = EmailForm(request.POST, instance=email)

        if form.is_valid():
            form.save()

            return render(request, 'emails/index.html', {
                'form': form,
                'success': True,
            })
    else:
        email = Email.objects.get(id=id)
        form = EmailForm(instance=email)

    return render(request, 'emails/edit.html', {
        'form': form
    })

def delete_email(request, id):
    if request.method == 'POST':
        email = Email.objects.get(id=id)
        email.delete()

    return HttpResponseRedirect(reverse('view_emails'))

def view_questions(request):
    return render(request, 'questions/index.html', {
        'questions': Question.objects.all()
    })

def view_question(request, id):
    question = Question.objects.get(id=id)

    return HttpResponseRedirect(reverse('view_questions'))

def add_question(request):
    if request.method == 'POST':
        form = QuestionForm(request.POST)

        if form.is_valid():
            new_question = Question(
                question_text=form.cleaned_data['question_text']
            )

            new_question.save()

            return render(request, 'questions/index.html', {
                'form': QuestionForm(),
                'success': True,
            })
    else:
        form = QuestionForm()

    return render(request, 'questions/add.html', {
        'email': QuestionForm()
    })

def edit_question(request, id):
    if request.method == 'POST':
        question = Question.objects.get(id=id)
        form = QuestionForm(request.POST, instance=question)

        if form.is_valid():
            form.save()

            return render(request, 'questions/index.html', {
                'form': form,
                'success': True,
            })
    else:
        question = Question.objects.get(id=id)
        form = QuestionForm(instance=question)

    return render(request, 'questions/edit.html', {
        'form': form
    })

def delete_question(request, id):
    if request.method == 'POST':
        question = Question.objects.get(id=id)
        question.delete()

    return HttpResponseRedirect(reverse('view_questions'))