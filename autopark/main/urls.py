from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index),
    path('drivers/driver/', views.DriverView.as_view()),
    path('drivers/driver/<int:driver_id>/', views.DriverByIdView.as_view()),
    path('vehicles/vehicle/', views.VehicleView.as_view()),
    path('vehicles/vehicle/<int:vehicle_id>/', views.VehicleByIdView.as_view()),
    path('vehicles/set_driver/<int:vehicle_id>/', views.VehicleSetDriverView.as_view()),
]
