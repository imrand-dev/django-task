from django.urls import path
from . import views

urlpatterns = [
    path("", view=views.OrderListView.as_view(), name="order-list"),
    path("/add", view=views.AddOrdrList.as_view(), name="add-order")
]