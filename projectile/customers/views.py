from django.shortcuts import render
from django.views.generic import TemplateView, ListView

from .models import Customer




class CustomerListView(ListView):
    template_name = 'customers/customers.html'   
    model = Customer