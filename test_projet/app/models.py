from django.db import models
from django.utils import reverse

# Create your models here.
class Company(models.Model):
    name=models.CharField(max_length=30)
    location=models.CharField(max_length=40)
    ceo=models.CharField(max_length=30)

    def  get_absolute_url(self):
        return reverse('home')