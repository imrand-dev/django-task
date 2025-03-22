from django.shortcuts import render
from django.views.generic import ListView, CreateView

from . import models

class MedicineListView(ListView):
    model = models.Medicine
    template_name = 'medicines/medicine.html'


class MedicineStockListView(ListView):
    model = models.MedicineStock
    template_name = 'medicines/medicine-stock.html'


class MedicineAddListView(CreateView):
    model = models.Medicine
    fields = ["name", "brand_name", "category", "unit_price", "pack_size"]
    template_name = "medicines/add.html"

class MedicineStockAddListView(CreateView):
    model = models.MedicineStock
    fields = ["medicine_name", "total_pack", "purchase_price"]
    template_name = "medicines/add-stock.html"

class MedicineCategory(ListView):
    model = models.Category
    template_name = "medicines/category.html"

class LowStockMedicineListView(ListView):
    model = models.Medicine
    template_name = 'medicines/low-stock.html'

class AddCategory(CreateView):
    model = models.Category
    fields = ["category_name"]
    template_name = "medicines/add-category.html"