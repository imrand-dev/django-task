from django.urls import path
from . import views

urlpatterns = [
    path("", views.MedicineListView.as_view(), name="medicine"),
    path("/stock", views.MedicineStockListView.as_view(), name="medicine-stock"),
    path("/add", views.MedicineAddListView.as_view(), name="add-medicine"),
    path("/stock/add", views.MedicineStockAddListView.as_view(), name="add-stock"),
    path("/category", views.MedicineCategory.as_view(), name="categories"),
    path("/low-stock", views.LowStockMedicineListView.as_view(), name="low-stocks"),
    path("/category/add", views.AddCategory.as_view(), name="add-category")
]
