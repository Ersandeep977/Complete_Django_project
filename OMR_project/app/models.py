from django.db import models

# Create your models here.
class Employes(models.Model):
    Eid=models.IntegerField()
    EName=models.CharField(max_length=30)
    ESal=models.FloatField()
    Eaddress=models.CharField(max_length=100)
    Eemail=models.EmailField()
    phoneno=models.IntegerField()