from django.contrib import admin
from RApp.models import Employee

# Register your models here.
class EmployessAdmin(admin.ModelAdmin):
    list_display = ['EmpID','FirstName','LstName']
admin.site.register(Employee,EmployessAdmin)
