from django.db import models


# Create your models here.
class Employes(models.Model):
    ENo=models.IntegerField()
    EName=models.CharField(max_length=30)
    ESal=models.IntegerField()
    EAddr=models.CharField(max_length=50)


