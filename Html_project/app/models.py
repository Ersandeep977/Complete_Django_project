from django.db import models
from django.utils import timezone

# Create your models here.
class Blog(models.Model):

    title = models.CharField(max_length=256)
    slug = models.SlugField(max_length=256)
    body = models.TextField()
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)



