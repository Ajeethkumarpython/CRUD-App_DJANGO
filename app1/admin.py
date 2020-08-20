from django.contrib import admin
from .models import Employee
# Register your models here.
class EmployeeAdmin(admin.ModelAdmin):
    list_display= ['Emp_ID', 'Emp_Name', 'Experience', 'Salary', 'Address', 'Tech_Skills']
admin.site.register(Employee,EmployeeAdmin)