from django.contrib import admin
from RApp.models import Student

# Register your models here.
class StudentAdmin(admin.ModelAdmin):
    list_display = ['stdid','stdName','stdGrade','stdRest']
admin.site.register(Student,StudentAdmin)
