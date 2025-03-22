from django.shortcuts import render

from django.views.generic import ListView, TemplateView, CreateView

from .models import Employee

class HomePageView(TemplateView):
    template_name = 'index.html'

class EmployeeListView(ListView):
    template_name = 'users/employee.html'   
    model = Employee

class AddEmployee(CreateView):
    model = Employee
    fields = ["user", "phone", "address", "profile_image", "role"]
    template_name = "users/add-employee.html"