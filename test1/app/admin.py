from django.contrib import admin
from app.models import StudentDatabase,FeeDept
# Register your models here.


class StudentDatabaseAdmin(admin.ModelAdmin):
    list_display = ('student_name', 'fathers_name', 'gender', 'branch', 'actual_fees', 'concession', 'net_pay', 'currently_paid', 'balance')


class FeeDeptAdmin(admin.ModelAdmin):
    list_display = ('student_name1', 'fee_type', 'fees_amount', 'balance', 'dos')


admin.site.register(StudentDatabase, StudentDatabaseAdmin,)
admin.site.register(FeeDept, FeeDeptAdmin,)
admin.site.site_header = 'Admin | College'
admin.site.index_title = 'college '
