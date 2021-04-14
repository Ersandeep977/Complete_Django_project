from django.contrib import admin
from BlogApp.models import Post

# Register your models here.

class PostAdmin(admin.ModelAdmin):
     list_display =['title','slug','','body','publish','created','update','status']
admin.site.register(Post,PostAdmin)

