from django.urls import path

from . import views

urlpatterns = [
    path("", view=views.HomePageView.as_view(), name="home"),
    path("/employees", view=views.EmployeeListView.as_view(), name="employees"),
    path("/employees/add", views.AddEmployee.as_view(), name="add-employee"),
]