from django.contrib import admin
from app.models import Blog

# Register your models here.
class BlogAdmin(admin.ModelAdmin):
    list_display = ['id','title','slug','body','publish','created','update']

admin.site.register(Blog)
