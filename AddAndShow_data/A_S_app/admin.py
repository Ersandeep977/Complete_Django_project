from django.contrib import admin
from A_S_app.models import Movies

# Register your models here.
class MoviesAdmin(admin.ModelAdmin):
    list_display = ['id','RDate','MovieName','HeroName','HeroineName','Rating']

admin.site.register(Movies,MoviesAdmin)

