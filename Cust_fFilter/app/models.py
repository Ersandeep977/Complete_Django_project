from django.db import models

# Create your models here.
class Movies(models.Model):
    RDate=models.DateField()
    MovieName=models.CharField(max_length=30)
    HeroName=models.CharField(max_length=30)
    HeroineName=models.CharField(max_length=30)
    Rating=models.IntegerField()