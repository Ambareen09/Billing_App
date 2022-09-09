from django.urls import path, include

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("viewinventory", views.InventoryView.as_view(),
         name="inventoryView"),
    path("addinventory", views.AddInventoryView.as_view(),
         name="addinventory"),
    path("viewitem/<str:pk>", views.ItemView.as_view(),
         name="viewitem"),
    path("edititem/<str:pk>", views.EdititemView.as_view(),
         name="viewitem"),


    path("addbilling", views.AddBillingView.as_view(),
         name="addbilling"),
    path("billinghistory", views.BillingHistoryView.as_view(),
         name="billinghistory"),
    path("viewbill/<str:pk>", views.BillView.as_view(),
         name="viewbill"),


    path("expense", views.ExpenseView.as_view(),
         name="expense"),
    path("addexpense", views.AddExpenseView.as_view(),
         name="addexpense"),
    path("editexpense/<str:pk>", views.EditExpenseView.as_view(),
         name="editexpense"),
    path("viewexpense/<str:pk>", views.ViewExpenseView.as_view(),
         name="viewexpense"),


    path("salary", views.SalaryView.as_view(),
         name="salary"),
    path("addsalary", views.AddSalaryView.as_view(),
         name="addsalary"),
    path("editsalary/<str:pk>", views.EditSalaryView.as_view(),
         name="editsalary"),
    path("viewsalary/<str:pk>", views.ViewSalaryView.as_view(),
         name="viewsalary"),


    path("pendingbills", views.PendingBillsView.as_view(),
         name="pendingbills"),
    path("viewunpaidbill", views.ViewPendingBillsView.as_view(),
         name="viewunpaidbill"),


    path("vendor", views.VendorView.as_view(),
         name="vendor"),
    path("viewvendor/<str:pk>", views.ViewVendorView.as_view(),
         name="viewvendor"),
    path("editvendor/<str:pk>", views.EditVendorView.as_view(),
         name="editvendor"),
    path("addvendor", views.AddVendorView.as_view(),
         name="addvendor"),


    path("staff", views.StaffView.as_view(),
         name="staff"),
    path("addstaff", views.AddStaffView.as_view(),
         name="addstaff"),
    path("viewstaff/<str:pk>", views.ViewStaffView.as_view(),
         name="viewstaff"),


    path("customer", views.CustomerView.as_view(),
         name="customer"),
    path("addcustomer", views.AddCustomerView.as_view(),
         name="addcustomer"),
    path("viewcustomer/<str:pk>", views.ViewCustomerView.as_view(),
         name="viewcustomer"),



    path("addstock", views.AddStockView.as_view(),
         name="addstock"),



]
