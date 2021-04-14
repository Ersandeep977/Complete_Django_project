from django.contrib import admin
from  Mapp.models import  Emp

# Register your models here.
class EmpAdmin(admin.ModelAdmin):
    list_display = ['Eid','EName','ESalary','Eloc','EPos']

admin.site.register(Emp,EmpAdmin)
