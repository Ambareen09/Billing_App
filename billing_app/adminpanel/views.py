from django.shortcuts import render, redirect
import traceback

from django.views import View
from django.forms import model_to_dict
from adminpanel.models import Billing, Customer, Expense, ExpenseType, Inventory, PayMode, Salary, Staff, Vendor
from adminpanel.serializers import (
    BillingDetailSerializer,
    ExpenseDetailSerializer,
    InventoryDetailSerializer
)
from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView


# Create your views here.


def index(request):
    return render(request, "adminpanel/index.html")


class BaseAPIView(APIView):
    def handle_exception(self, exc):
        try:
            return super(BaseAPIView, self).handle_exception(exc)
        except Exception as e:
            tb = traceback.format_exc()
            return Response({"error": tb}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


def get_obj(obj_name):
    return obj_name.objects.all()


class InventoryView(BaseAPIView):
    def get(self, request):
        inventory = [model_to_dict(b) for b in Inventory.objects.all()]
        return render(
            request,
            "adminpanel/viewinventory.html",
            {"inventory": inventory},
        )


class AddInventoryView(BaseAPIView):
    def get(self, request):
        return render(request, "adminpanel/addinventory.html")

    def post(self, request):
        serializer = InventoryDetailSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return redirect('/viewinventory')
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class AddBillingView(BaseAPIView):
    def get(self, request):
        return render(request, "adminpanel/addbilling.html")


class BillingHistoryView(BaseAPIView):
    def get(self, request):
        billinghistory = Billing.objects.all()
        return render(
            request,
            "adminpanel/billinghistory.html",
            {"billinghistory": billinghistory},
        )


class ExpenseView(BaseAPIView):
    def get(self, request):
        expense = Expense.objects.all()
        return render(
            request,
            "adminpanel/expense.html",
            {"expense": expense},
        )


class AddExpenseView(BaseAPIView):
    def get(self, request):
        expense_type = get_obj(ExpenseType)
        vendor_name = get_obj(Vendor)
        pay_mode = get_obj(PayMode)

        return render(
            request,
            "adminpanel/addexpense.html",
            {"expense_type": expense_type, "vendor_name": vendor_name,
                "pay_mode": pay_mode},
        )

    def post(self, request):
        serializer = ExpenseDetailSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return redirect('/expense')
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class SalaryView(BaseAPIView):
    def get(self, request):
        salary = Salary.objects.all()
        return render(
            request,
            "adminpanel/salary.html",
            {"salary": salary},
        )


class PendingBillsView(BaseAPIView):
    def get(self, request):
        pendingbills = Billing.objects.all()
        return render(
            request,
            "adminpanel/pendingbills.html",
            {"pendingbills": pendingbills},
        )


class ViewPendingBillsView(BaseAPIView):
    def get(self, request):
        return render(request, "adminpanel/viewunpaidbill.html")


class VendorView(BaseAPIView):
    def get(self, request):
        vendor = Vendor.objects.all()
        return render(
            request,
            "adminpanel/vendor.html",
            {"vendor": vendor},
        )


class ViewVendorView(BaseAPIView):
    def get(self, request):
        return render(request, "adminpanel/viewvendor.html")


class AddVendorView(BaseAPIView):
    def get(self, request):
        return render(request, "adminpanel/addvendor.html")


class StaffView(BaseAPIView):
    def get(self, request):
        staff = Staff.objects.all()
        return render(
            request,
            "adminpanel/staff.html",
            {"staff": staff},
        )


class AddStaffView(BaseAPIView):
    def get(self, request):
        return render(request, "adminpanel/addstaff.html")


class ViewStaffView(BaseAPIView):
    def get(self, request):
        return render(request, "adminpanel/viewstaff.html")


class CustomerView(BaseAPIView):
    def get(self, request):
        customer = Customer.objects.all()
        return render(
            request,
            "adminpanel/customer.html",
            {"customer": customer},
        )

        return render(request, "adminpanel/customer.html")


class AddCustomerView(BaseAPIView):
    def get(self, request):
        return render(request, "adminpanel/addcustomer.html")


class ViewCustomerView(BaseAPIView):
    def get(self, request):
        return render(request, "adminpanel/viewcustomer.html")


class ItemView(BaseAPIView):
    def get(self, request):
        return render(request, "adminpanel/addviewitem.html")


class AddStockView(BaseAPIView):
    def get(self, request):
        return render(request, "adminpanel/addstock.html")


class BillView(BaseAPIView):
    def get(self, request):
        return render(request, "adminpanel/viewbill.html")


class ViewSalaryView(BaseAPIView):
    def get(self, request):
        return render(request, "adminpanel/viewsalary.html")


class EditExpenseView(BaseAPIView):
    def get(self, request):
        return render(request, "adminpanel/editexpense.html")


class ViewExpenseView(BaseAPIView):
    def get(self, request):
        return render(request, "adminpanel/viewexpense.html")
