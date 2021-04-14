from django.db import models

# Create your models here.
class Hyd_jobs(models.Model):
    date=models.DateField()
    company=models.CharField(max_length=100)
    title=models.CharField(max_length=100)
    elisbility=models.CharField(max_length=100)
    address=models.CharField(max_length=100)
    email=models.EmailField()
    phoneno=models.IntegerField()

class Pune_jobs(models.Model):
    date=models.DateField()
    company=models.CharField(max_length=100)
    title=models.CharField(max_length=100)
    elisbility=models.CharField(max_length=100)
    address=models.CharField(max_length=100)
    email=models.EmailField()
    phoneno=models.IntegerField()

class Chann_jobs(models.Model):
    date=models.DateField()
    company=models.CharField(max_length=100)
    title=models.CharField(max_length=100)
    elisbility=models.CharField(max_length=100)
    address=models.CharField(max_length=100)
    email=models.EmailField()
    phoneno=models.IntegerField()

