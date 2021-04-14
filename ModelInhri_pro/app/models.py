from django.db import models

# Create your models here.
class CustomManger1(models.Manager):
    def get_queryset(self):
        return super().get_queryset()

class CustomManger2(models.Manager):
    def get_queryset(self):
        return super().get_queryset().order_by('EName')


class Employes(models.Model):
    Eid=models.IntegerField()
    EName=models.CharField(max_length=30)
    ESal=models.FloatField()
    Eaddress=models.CharField(max_length=100)
    Eemail=models.EmailField()
    phoneno=models.IntegerField()
    objects=CustomManger1()

class ProxyEmployes(Employes):
    objects = CustomManger2()
    class Meta:
        proxy=True
