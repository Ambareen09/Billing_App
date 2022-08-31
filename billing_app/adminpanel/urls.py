from django.urls import path, include

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("viewinventory", views.InventoryView.as_view(),
         name="inventoryView"),
    path("addinventory", views.AddInventoryView.as_view(),
         name="addinventory"),
    path("addbilling", views.AddBillingView.as_view(),
         name="addbilling"),
    path("billinghistory", views.BillingHistoryView.as_view(),
         name="billinghistory"),
    path("expense", views.ExpenseView.as_view(),
         name="expense"),
    path("salary", views.SalaryView.as_view(),
         name="salary"),
    path("pendingbills", views.PendingBillsView.as_view(),
         name="pendingbills"),
    path("vendor", views.VendorView.as_view(),
         name="vendor"),
    path("staff", views.StaffView.as_view(),
         name="staff"),
    path("customer", views.CustomerView.as_view(),
         name="customer"),
    path("viewitem", views.ItemView.as_view(),
         name="viewitem"),
]
