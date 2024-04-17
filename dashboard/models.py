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