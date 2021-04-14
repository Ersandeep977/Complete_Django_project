from django.contrib import admin
from app.models import Employee

# Register your models here.
class EmployesAdmin(admin.ModelAdmin):
    list_display = ['id','eno','ename','esal','eadd']
admin.site.register(Employee,EmployesAdmin)