from django.db import models

# Create your models here.
class Email(models.Model):
    email = models.EmailField()
    name = models.CharField(max_length=100)
    subject = models.CharField(max_length=100)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Email: {self.email} - {self.subject}'
    
class Question(models.Model):
    question_text = models.CharField(max_length=200, blank=False, null=False, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.question_text
    
class Response(models.Model):
    question = models.ForeignKey(Question, on_delete=models.PROTECT)
    response = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.response

class TeamMember(models.Model):
    name = models.CharField(max_length=100)
    designation = models.CharField(max_length=100)
    bio = models.TextField()
    icon = models.CharField(max_length=5)
    position = models.PositiveIntegerField()
    active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self) -> str:
        return f'Member: {self.name} - {self.designation}'
    
class TeamMember(models.Model):
    name = models.CharField(max_length=100)
    designation = models.CharField(max_length=100)
    bio = models.TextField()
    icon = models.CharField(max_length=5)
    position = models.PositiveIntegerField()
    active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self) -> str:
        return f'Member: {self.name} - {self.designation}'
    