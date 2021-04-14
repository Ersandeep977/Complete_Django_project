from django.contrib import admin
from app.models import Student,Teacher

# Register your models here.
class StudentAdmin(admin.ModelAdmin):
    list_display = ['id','name','email','address','rollno','mark']
admin.site.register(Student,StudentAdmin)

class TeacherAdmin(admin.ModelAdmin):
    list_display = ['id','name','email','address','Subject','salary']
admin.site.register(Teacher,TeacherAdmin)
