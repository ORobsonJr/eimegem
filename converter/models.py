from django.db import models

# Create your models here.
class Word(models.Model):
    word = models.CharField(max_length=30, primary_key=True)
    frequency = models.IntegerField(default=0)