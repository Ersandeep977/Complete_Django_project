from django.db import models

# Create your models here.
class Employee(models.Model):
    EmpID=models.IntegerField()
    FirstName=models.CharField(max_length=100)
    LstName=models.CharField(max_length=100)

    def __str__(self):
        return self.FirstName