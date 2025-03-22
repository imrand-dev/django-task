from django.contrib import admin
from customers.models import Customer

@admin.register(Customer)
class CustomerModelAdmin(admin.ModelAdmin):
    list_display = ["name", "phone"]
