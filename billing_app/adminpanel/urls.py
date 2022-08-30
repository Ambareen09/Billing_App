from django.urls import path, include

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("viewinventory", views.InventoryView.as_view(),
         name="inventoryView"),
]
