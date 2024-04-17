from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('emails/', views.view_emails, name='view_emails'),
    path('emails/<int:id>', views.view_email, name='view_email'),
    path('emails/add/', views.add_email, name='add_email'),
    path('emails/edit/<int:id>', views.edit_email, name='edit_email'),
    path('emails/delete/<int:id>', views.delete_email, name='delete_email'),
    path('questions/', views.view_questions, name='view_questions'),
    path('questions/<int:id>', views.view_question, name='view_question'),
    path('questions/add/', views.add_question, name='add_question'),
    path('questions/edit/<int:id>', views.edit_question, name='edit_question'),
    path('questions/delete/<int:id>', views.delete_question, name='delete_question'),
    path('responses/', views.view_responses, name='view_responses'),
    path('responses/<int:id>', views.view_response, name='view_response'),
    path('responses/add/', views.add_response, name='add_response'),
    path('responses/edit/<int:id>', views.edit_response, name='edit_response'),
    path('responses/delete/<int:id>', views.delete_response, name='delete_response'),
]