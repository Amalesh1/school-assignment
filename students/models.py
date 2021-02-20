from django.db import models
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your models here.
class Contact(models.Model):
    name=models.CharField(max_length=50)
    email=models.CharField(max_length=100)
    Class=models.CharField(max_length=20)
    desc=models.TextField()
    date=models.DateField()

    def __str__(self):
        return self.name

class EnglishAssignment(models.Model):
    roll=models.CharField(max_length=20)
    topics=models.CharField(max_length=150)
    dept=models.CharField(max_length=200)
    sem=models.CharField(max_length=200)
    ans=models.TextField()
    date=models.DateField()
    time=models.TimeField()

    def __str__(self):
        return self.roll

class PhysicsAssignment(models.Model):
    roll=models.CharField(max_length=20)
    topics=models.CharField(max_length=150)
    dept=models.CharField(max_length=200)
    sem=models.CharField(max_length=200)
    ans=models.TextField()
    date=models.DateField()
    time=models.TimeField()

    def __str__(self):
        return self.roll

class MathAssignment(models.Model):
    roll=models.CharField(max_length=20)
    topics=models.CharField(max_length=150)
    dept=models.CharField(max_length=200)
    sem=models.CharField(max_length=200)
    ans=models.TextField()
    date=models.DateField()
    time=models.TimeField()

    def __str__(self):
        return self.roll


