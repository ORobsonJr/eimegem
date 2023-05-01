from django.db import models

# Create your models here.

"""
Models is empty because we don't wan't to store anything
"""
class Word(models.Model):
    word = models.CharField(max_length=30, primary_key=True)
    frequency = models.IntegerField()