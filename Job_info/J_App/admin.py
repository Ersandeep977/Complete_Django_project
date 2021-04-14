from django.contrib import admin
from J_App.models import Hyd_jobs,Pune_jobs,Chann_jobs

# Register your models here.
class HydJobAdmin(admin.ModelAdmin):
    list_display = ['id','date','company','title','elisbility','address','email','phoneno']

class PuneJobAdmin(admin.ModelAdmin):
    list_display = ['id', 'date', 'company', 'title', 'elisbility', 'address', 'email', 'phoneno']

class ChannJobAdmin(admin.ModelAdmin):
    list_display = ['id', 'date', 'company', 'title', 'elisbility', 'address', 'email', 'phoneno']

admin.site.register(Hyd_jobs,HydJobAdmin)
admin.site.register(Pune_jobs,PuneJobAdmin)
admin.site.register(Chann_jobs,ChannJobAdmin)
