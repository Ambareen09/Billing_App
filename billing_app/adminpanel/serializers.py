from operator import mod
from pyexpat import model
from rest_framework import serializers
from adminpanel.models import (
    Billing,
    Expense,
    Inventory,
    Salary
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
    expense_detail = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Salary
        fields = "__all__"
