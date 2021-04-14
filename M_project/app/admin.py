from django.contrib import admin
from app.models import Movies
# Register your models here.
class MovieAdmin(admin.ModelAdmin):
    list_display = ['rdate','moviename','hero','heroine','rating']
admin.site.register(Movies,MovieAdmin)