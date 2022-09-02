from operator import mod
from pyexpat import model
from rest_framework import serializers
from adminpanel.models import (
    Billing,
    Customer,
    Expense,
    Inventory,
    Salary,
    Staff,
    Vendor
)


class BillingDetailSerializer(serializers.ModelSerializer):
    billing_detail = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Billing
        fields = "__all__"


class InventoryDetailSerializer(serializers.ModelSerializer):
    inventory_detail = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Inventory
        fields = "__all__"


class ExpenseDetailSerializer(serializers.ModelSerializer):
    expense_detail = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Expense
        fields = "__all__"


class SalaryDetailSerializer(serializers.ModelSerializer):
    salary_detail = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Salary
        fields = "__all__"


class VendorDetailSerializer(serializers.ModelSerializer):
    vendor_detail = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Vendor
        fields = "__all__"


class CustomerDetailSerializer(serializers.ModelSerializer):
    customer_detail = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Customer
        fields = "__all__"


class StaffDetailSerializer(serializers.ModelSerializer):
    staff_detail = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Staff
        fields = "__all__"
