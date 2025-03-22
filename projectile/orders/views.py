from django.shortcuts import render
from django.views.generic import ListView, CreateView

from . import models

class OrderListView(ListView):
    model = models.Order
    template_name = 'orders/order.html'

class AddOrdrList(CreateView):
    model = models.Order 
    fields = ["medicine", "customer"]
    template_name = "orders/add-order.html"