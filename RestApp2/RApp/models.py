from django.db import models

# Create your models here.
class Student(models.Model):
    stdid=models.IntegerField()
    stdName=models.CharField(max_length=100)
    stdGrade=models.CharField(max_length=10)
    stdRest=models.CharField(max_length=10)
