from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse

from .models import *
from .forms import *

# Create your views here.

# Dashboard
def index(request):
    return render(request, 'dashboard/index.html')

# Emails
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

# Questions
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
        'question': QuestionForm()
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

# Responses
def view_responses(request):
    return render(request, 'responses/index.html', {
        'responses': Response.objects.all()
    })

def view_response(request, id):
    response = Response.objects.get(id=id)

    return HttpResponseRedirect(reverse('view_responses'))

def add_response(request):
    if request.method == 'POST':
        form = ResponseForm(request.POST)

        if form.is_valid():
           new_response = Response(
                question=form.cleaned_data['question'],
                response=form.cleaned_data['response']
            )
    else:
        form = ResponseForm()

    return render(request, 'responses/add.html', {
        'response': ResponseForm()
    })

def edit_response(request, id):
    if request.method == 'POST':
        response = Response.objects.get(id=id)
        form = ResponseForm(request.POST, instance=response)

        if form.is_valid():
            form.save()

            return render(request, 'responses/index.html', {
                'form': form,
                'success': True,
            })
    else:
        response = Response.objects.get(id=id)
        form = ResponseForm(instance=response)

    return render(request, 'responses/edit.html', {
        'form': form
    })

def delete_response(request, id):
    if request.method == 'POST':
        response = Response.objects.get(id=id)
        response.delete()

    return HttpResponseRedirect(reverse('view_responses'))
