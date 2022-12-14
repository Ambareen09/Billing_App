from django.shortcuts import render, redirect
import traceback

from django.views import View
from django.forms import model_to_dict
from adminpanel.models import Billing, Customer, Expense, ExpenseType, Inventory, PayMode, Salary, Staff, StaffType, Vendor, VendorType
from adminpanel.serializers import (
    BillingDetailSerializer,
    CustomerDetailSerializer,
    ExpenseDetailSerializer,
    InventoryDetailSerializer,
    SalaryDetailSerializer,
    StaffDetailSerializer,
    VendorDetailSerializer
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


class ItemView(BaseAPIView):
    def get(self, request, pk):
        if not Inventory.objects.filter(pk=pk).exists():
            return Response(
                {"Error": "item does not exist"}, status=status.HTTP_404_NOT_FOUND
            )
        item = Inventory.objects.get(pk=pk)
        serializer = InventoryDetailSerializer(
            item, context={"request": request})
        return render(
            request,
            "adminpanel/viewitem.html",
            {"i": item},
        )


class EdititemView(BaseAPIView):
    def get(self, request, pk):
        if not Inventory.objects.filter(pk=pk).exists():
            return Response(
                {"Error": "item does not exist"}, status=status.HTTP_404_NOT_FOUND
            )
        item = Inventory.objects.get(pk=pk)
        serializer = InventoryDetailSerializer(
            item, context={"request": request})
        return render(
            request,
            "adminpanel/edititem.html",
            {"i": item},
        )

    def put(self, request, pk):
        item = Inventory.objects.get(pk=pk)
        serializer = InventoryDetailSerializer(item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        if Inventory.objects.filter(pk=pk).exists():
            Inventory.objects.get(pk=pk).delete()
        return HttpResponse({"msg": "successful"})


class BillView(BaseAPIView):
    def get(self, request, pk):
        if not Billing.objects.filter(pk=pk).exists():
            return Response(
                {"Error": "bill does not exist"}, status=status.HTTP_404_NOT_FOUND
            )
        bill = Billing.objects.get(pk=pk)
        serializer = BillingDetailSerializer(
            bill, context={"request": request})
        return render(
            request,
            "adminpanel/viewbill.html",
            {"b": bill},
        )


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


class EditExpenseView(BaseAPIView):
    def get(self, request, pk):
        if not Expense.objects.filter(pk=pk).exists():
            return Response(
                {"Error": "Expense does not exist"}, status=status.HTTP_404_NOT_FOUND
            )
        expense = Expense.objects.get(pk=pk)
        expense_type = get_obj(ExpenseType)
        vendor_name = get_obj(Vendor)
        pay_mode = get_obj(PayMode)

        return render(
            request,
            "adminpanel/editexpense.html",
            {"expense_type": expense_type, "ex": expense, "vendor_name": vendor_name,
                "pay_mode": pay_mode},
        )

    def put(self, request, pk):
        expense = Expense.objects.get(pk=pk)
        serializer = ExpenseDetailSerializer(expense, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        if Expense.objects.filter(pk=pk).exists():
            Expense.objects.get(pk=pk).delete()
        return HttpResponse({"msg": "successful"})


class ViewExpenseView(BaseAPIView):
    def get(self, request, pk):
        if not Expense.objects.filter(pk=pk).exists():
            return Response(
                {"Error": "Expense does not exist"}, status=status.HTTP_404_NOT_FOUND
            )
        expense = Expense.objects.get(pk=pk)
        serializer = ExpenseDetailSerializer(
            expense, context={"request": request})
        return render(
            request,
            "adminpanel/viewexpense.html",
            {"e": expense},
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


class AddSalaryView(BaseAPIView):
    def get(self, request):
        staff_type = get_obj(Staff)
        pay_mode = get_obj(PayMode)

        return render(
            request,
            "adminpanel/addsalary.html",
            {"staff_type": staff_type,
             "pay_mode": pay_mode},
        )

    def post(self, request):
        serializer = SalaryDetailSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return redirect('/salary')
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ViewSalaryView(BaseAPIView):
    def get(self, request, pk):
        if not Salary.objects.filter(pk=pk).exists():
            return Response(
                {"Error": "Salary does not exist"}, status=status.HTTP_404_NOT_FOUND
            )
        salary = Salary.objects.get(pk=pk)
        serializer = SalaryDetailSerializer(
            salary, context={"request": request})
        return render(
            request,
            "adminpanel/viewsalary.html",
            {"s": salary, },
        )


class EditSalaryView(BaseAPIView):
    def get(self, request, pk):
        if not Salary.objects.filter(pk=pk).exists():
            return Response(
                {"Error": "Salary does not exist"}, status=status.HTTP_404_NOT_FOUND
            )
        salary = Salary.objects.get(pk=pk)
        staff_type = get_obj(Staff)
        pay_mode = get_obj(PayMode)

        return render(
            request,
            "adminpanel/editsalary.html",
            {"s": salary, "staff_type": staff_type,
             "pay_mode": pay_mode},
        )

    def put(self, request, pk):
        salary = Salary.objects.get(pk=pk)
        serializer = SalaryDetailSerializer(salary, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        if Salary.objects.filter(pk=pk).exists():
            Salary.objects.get(pk=pk).delete()
        return HttpResponse({"msg": "successful"})


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
    def get(self, request, pk):
        if not Vendor.objects.filter(pk=pk).exists():
            return Response(
                {"Error": "Vendor does not exist"}, status=status.HTTP_404_NOT_FOUND
            )
        vendor = Vendor.objects.get(pk=pk)
        serializer = VendorDetailSerializer(
            vendor, context={"request": request})
        return render(
            request,
            "adminpanel/viewvendor.html",
            {"v": vendor},
        )


class EditVendorView(BaseAPIView):
    def get(self, request, pk):
        if not Vendor.objects.filter(pk=pk).exists():
            return Response(
                {"Error": "Vendor does not exist"}, status=status.HTTP_404_NOT_FOUND
            )
        vendor = Vendor.objects.get(pk=pk)
        vendor_type_name = get_obj(VendorType)
        serializer = VendorDetailSerializer(
            vendor, context={"request": request})
        return render(
            request,
            "adminpanel/editvendor.html",
            {"v": vendor, "vendor_type_name": vendor_type_name},
        )

    def put(self, request, pk):
        vendor = Vendor.objects.get(pk=pk)
        serializer = VendorDetailSerializer(vendor, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        if Vendor.objects.filter(pk=pk).exists():
            Vendor.objects.get(pk=pk).delete()
        return HttpResponse({"msg": "successful"})


class AddVendorView(BaseAPIView):

    def get(self, request):
        vendor_type_name = get_obj(VendorType)

        return render(
            request,
            "adminpanel/addvendor.html",
            {"vendor_type_name": vendor_type_name}
        )

    def post(self, request):
        serializer = VendorDetailSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return redirect('/vendor')
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class StaffView(BaseAPIView):
    def get(self, request):
        staff = Staff.objects.all()
        return render(
            request,
            "adminpanel/staff.html",
            {"staff": staff},
        )


class EditStaffView(BaseAPIView):
    def get(self, request, pk):
        if not Staff.objects.filter(pk=pk).exists():
            return Response(
                {"Error": "Staff does not exist"}, status=status.HTTP_404_NOT_FOUND
            )
        staff = Staff.objects.get(pk=pk)
        staff_type_name = get_obj(StaffType)
        serializer = StaffDetailSerializer(
            staff, context={"request": request})
        return render(
            request,
            "adminpanel/editstaff.html",
            {"s": staff, "staff_type_name": staff_type_name},
        )

    def put(self, request, pk):
        staff = Staff.objects.get(pk=pk)
        serializer = StaffDetailSerializer(staff, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        if Staff.objects.filter(pk=pk).exists():
            Staff.objects.get(pk=pk).delete()
        return HttpResponse({"msg": "successful"})


class AddStaffView(BaseAPIView):
    def get(self, request):
        staff_type_name = get_obj(StaffType)
        return render(request,
                      "adminpanel/addstaff.html",
                      {"staff_type_name": staff_type_name})

    def post(self, request):
        serializer = StaffDetailSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return redirect('/staff')
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ViewStaffView(BaseAPIView):
    def get(self, request, pk):
        if not Staff.objects.filter(pk=pk).exists():
            return Response(
                {"Error": "Staff does not exist"}, status=status.HTTP_404_NOT_FOUND
            )
        staff = Staff.objects.get(pk=pk)
        serializer = StaffDetailSerializer(
            staff, context={"request": request})
        return render(
            request,
            "adminpanel/viewstaff.html",
            {"s": staff},
        )


class CustomerView(BaseAPIView):
    def get(self, request):
        customer = Customer.objects.all()
        return render(
            request,
            "adminpanel/customer.html",
            {"customer": customer},
        )


class EditCustomerView(BaseAPIView):
    def get(self, request, pk):
        if not Customer.objects.filter(pk=pk).exists():
            return Response(
                {"Error": "Customer does not exist"}, status=status.HTTP_404_NOT_FOUND
            )
        customer = Customer.objects.get(pk=pk)

        return render(
            request,
            "adminpanel/editcustomer.html",
            {"c": customer},
        )

    def put(self, request, pk):
        customer = Customer.objects.get(pk=pk)
        serializer = CustomerDetailSerializer(customer, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        if Customer.objects.filter(pk=pk).exists():
            Customer.objects.get(pk=pk).delete()
        return HttpResponse({"msg": "successful"})


class AddCustomerView(BaseAPIView):
    def get(self, request):
        return render(request, "adminpanel/addcustomer.html")

    def post(self, request):
        serializer = CustomerDetailSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return redirect('/customer')
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ViewCustomerView(BaseAPIView):
    def get(self, request, pk):
        if not Customer.objects.filter(pk=pk).exists():
            return Response(
                {"Error": "Customer does not exist"}, status=status.HTTP_404_NOT_FOUND
            )
        customer = Customer.objects.get(pk=pk)
        serializer = CustomerDetailSerializer(
            customer, context={"request": request})
        return render(
            request,
            "adminpanel/viewcustomer.html",
            {"c": customer},
        )


class AddStockView(BaseAPIView):
    def get(self, request):
        return render(request, "adminpanel/addstock.html")
