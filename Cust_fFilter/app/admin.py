from django.contrib import admin
from app.models import Movies

# Register your models here.
class MoviesAdmin(admin.ModelAdmin):
    list_display = ['id','RDate','MovieName','HeroName','HeroineName','Rating']

admin.site.register(Movies,MoviesAdmin)

