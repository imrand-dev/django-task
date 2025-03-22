from django.urls import path

from . import views

urlpatterns = [
    path("", view=views.CustomerListView.as_view(), name="customers"),
]
