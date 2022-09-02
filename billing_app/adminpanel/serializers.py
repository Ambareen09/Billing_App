from operator import mod
from pyexpat import model
from rest_framework import serializers
from adminpanel.models import (
    Billing,
    Inventory
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
