from django.db import models
from django.forms import widgets

# Create your models here.

class UserFeedback(models.Model):
    name=models.CharField(max_length=70)
    email=models.EmailField(max_length=40)
    feedback=models.CharField(max_length=800)
    date = models.DateTimeField("Date")

    def __str__(self):
        return f'{self.name}:: {self.feedback}'

