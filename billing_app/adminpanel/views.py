from django.shortcuts import render, redirect
from django.views import View

# Create your views here.


def index(request):
    return render(request, "adminpanel/index.html")


class InventoryView(View):
    def get(self, request):
        return render(request, "adminpanel/viewinventory.html")


class AddInventoryView(View):
    def get(self, request):
        return render(request, "adminpanel/addinventory.html")


class AddBillingView(View):
    def get(self, request):
        return render(request, "adminpanel/addbilling.html")


class BillingHistoryView(View):
    def get(self, request):
        return render(request, "adminpanel/billinghistory.html")


class ExpenseView(View):
    def get(self, request):
        return render(request, "adminpanel/expense.html")


class SalaryView(View):
    def get(self, request):
        return render(request, "adminpanel/salary.html")


class PendingBillsView(View):
    def get(self, request):
        return render(request, "adminpanel/pendingbills.html")


class VendorView(View):
    def get(self, request):
        return render(request, "adminpanel/vendor.html")


class StaffView(View):
    def get(self, request):
        return render(request, "adminpanel/staff.html")


class CustomerView(View):
    def get(self, request):
        return render(request, "adminpanel/customer.html")


class ItemView(View):
    def get(self, request):
        return render(request, "adminpanel/viewitem.html")
