from django.db import models

# Create your models here.
class ContactInfo(models.Model):
    name=models.CharField(max_length=40)
    email=models.EmailField()
    address=models.CharField(max_length=60)
    class Meta:
        abstract=True

class Student(ContactInfo):
    rollno=models.IntegerField()
    mark=models.IntegerField()

class Teacher(ContactInfo):
    Subject=models.CharField(max_length=50)
    salary=models.FloatField()



