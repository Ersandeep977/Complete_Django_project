from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.
class Post(models.Model):
    Status_Choices=(('draft','Draft'),('published','Published'))
    title=models.CharField(max_length=250)
    slug=models.SlugField(max_length=200,unique_for_date='published')
    #author=models.
    body=models.TextField()
    publish=models.DateTimeField(default=timezone.now())
    created=models.DateTimeField(auto_now_add=True)
    update=models.DateTimeField(auto_now=True)
    status=models.CharField(max_length=10,Choices=Status_Choices,default='draft')


    class Meta:
        ordering=('-publish',)

    def __str__(self):
         return self.title