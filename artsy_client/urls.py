from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('member/<int:id>', views.view_member_profile, name='view_member_profile'),
]