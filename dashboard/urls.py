from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('emails/', views.view_emails, name='view_emails'),
    path('emails/<int:id>', views.view_email, name='view_email'),
    path('emails/add/', views.add_email, name='add_email'),
    path('emails/edit/<int:id>', views.edit_email, name='edit_email'),
    path('emails/delete/<int:id>', views.delete_email, name='delete_email'),
]