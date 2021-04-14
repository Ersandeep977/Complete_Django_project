from django.db import models

# Create your models here.
class Emp(models.Model):
    Eid=models.IntegerField()
    EName=models.CharField(max_length=100)
    ESalary=models.FloatField()
    Eloc=models.CharField(max_length=100)
    EPos=models.CharField(max_length=100)