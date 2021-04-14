from django.contrib import admin
from E_App.models import Employes

class EmployeAdmin(admin.ModelAdmin):
    list_display = ['id','ENo','EName','ESal','EAddr']
# Register your models here.
admin.site.register(Employes,EmployeAdmin)


