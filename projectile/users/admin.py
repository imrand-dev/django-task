from django.contrib import admin
from users.models import Employee

@admin.register(Employee)
class EmployeeModelAdmin(admin.ModelAdmin):
    list_display = ["user", "role"]

