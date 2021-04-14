from django.contrib import admin
from app.models import Employes,ProxyEmployes
# Register your models here.
class EmployesAdmin(admin.ModelAdmin):
    list_display = ['id','Eid','EName','ESal','Eaddress','Eemail','phoneno']

admin.site.register(Employes,EmployesAdmin)

class ProEmployesAdmin(admin.ModelAdmin):
    list_display = ['id','Eid','EName','ESal','Eaddress','Eemail','phoneno']
admin.site.register(ProxyEmployes,ProEmployesAdmin)