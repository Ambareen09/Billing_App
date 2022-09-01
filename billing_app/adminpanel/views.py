from django.shortcuts import render, redirect
from django.views import View
from django.forms import model_to_dict
from adminpanel.models import Billing, Customer, Expense, Inventory, Salary, Staff, Vendor
from adminpanel.serializers import (
    BillingDetailSerializer
)


# Create your views here.


def index(request):
    return render(request, "adminpanel/index.html")


class InventoryView(View):
    def get(self, request):
        inventory = [model_to_dict(b) for b in Inventory.objects.all()]
        return render(
            request,
            "adminpanel/viewinventory.html",
            {"inventory": inventory},
        )


class AddInventoryView(View):
    def get(self, request):
        return render(request, "adminpanel/addinventory.html")


class AddBillingView(View):
    def get(self, request):
        return render(request, "adminpanel/addbilling.html")


class BillingHistoryView(View):
    def get(self, request):
        billinghistory = Billing.objects.all()
        return render(
            request,
            "adminpanel/billinghistory.html",
            {"billinghistory": billinghistory},
        )


class ExpenseView(View):
    def get(self, request):
        expense = Expense.objects.all()
        return render(
            request,
            "adminpanel/expense.html",
            {"expense": expense},
        )


class SalaryView(View):
    def get(self, request):
        salary = Salary.objects.all()
        return render(
            request,
            "adminpanel/salary.html",
            {"salary": salary},
        )


class PendingBillsView(View):
    def get(self, request):
        pendingbills = Billing.objects.all()
        return render(
            request,
            "adminpanel/pendingbills.html",
            {"pendingbills": pendingbills},
        )


class ViewPendingBillsView(View):
    def get(self, request):
        return render(request, "adminpanel/viewunpaidbill.html")


class VendorView(View):
    def get(self, request):
        vendor = Vendor.objects.all()
        return render(
            request,
            "adminpanel/vendor.html",
            {"vendor": vendor},
        )


class ViewVendorView(View):
    def get(self, request):
        return render(request, "adminpanel/viewvendor.html")


class AddVendorView(View):
    def get(self, request):
        return render(request, "adminpanel/addvendor.html")


class StaffView(View):
    def get(self, request):
        staff = Staff.objects.all()
        return render(
            request,
            "adminpanel/staff.html",
            {"staff": staff},
        )


class AddStaffView(View):
    def get(self, request):
        return render(request, "adminpanel/addstaff.html")


class ViewStaffView(View):
    def get(self, request):
        return render(request, "adminpanel/viewstaff.html")


class CustomerView(View):
    def get(self, request):
        customer = Customer.objects.all()
        return render(
            request,
            "adminpanel/customer.html",
            {"customer": customer},
        )

        return render(request, "adminpanel/customer.html")


class AddCustomerView(View):
    def get(self, request):
        return render(request, "adminpanel/addcustomer.html")


class ViewCustomerView(View):
    def get(self, request):
        return render(request, "adminpanel/viewcustomer.html")


class ItemView(View):
    def get(self, request):
        return render(request, "adminpanel/addviewitem.html")


class AddStockView(View):
    def get(self, request):
        return render(request, "adminpanel/addstock.html")


class BillView(View):
    def get(self, request):
        return render(request, "adminpanel/viewbill.html")


class ViewSalaryView(View):
    def get(self, request):
        return render(request, "adminpanel/viewsalary.html")


class EditExpenseView(View):
    def get(self, request):
        return render(request, "adminpanel/editexpense.html")


class ViewExpenseView(View):
    def get(self, request):
        return render(request, "adminpanel/viewexpense.html")
