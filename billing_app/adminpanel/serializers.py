from operator import mod
from pyexpat import model
from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from adminpanel.models import (
    Billing
)


class BillingDetailSerializer(serializers.ModelSerializer):
    billing_detail = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Billing
        fields = "__all__"
