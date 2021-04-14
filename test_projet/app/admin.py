from django.contrib import admin
from app.models import Company

# Register your models here.
class CompanyAdmin(admin.ModelAdmin):
    list_display = ['id','name','location','ceo']

admin.site.register(Company,CompanyAdmin)

