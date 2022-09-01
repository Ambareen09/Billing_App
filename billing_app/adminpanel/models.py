from http import server
from operator import mod
from django import forms
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator
from django.contrib.postgres.fields import ArrayField
from django.db import models
from django.contrib.auth.models import User
from django.forms import ModelForm
from datetime import datetime
from django.utils import timezone


PAYMENT_STATUS = {
    ("PAID", "PAID"),
    ("UNPAID", "UNPAID"),
}
# Create your models here.

ACTIVITY_STATUS = {
    ("ACTIVE", "ACTIVE"),
    ("INACTIVE", "INACTIVE"),
}


class Base(models.Model):
    created_on = models.DateTimeField(auto_now_add=True, null=True)
    updated_on = models.DateTimeField(
        auto_now_add=False, auto_now=True, null=True)

    class Meta:
        abstract = True


class PayMode(Base):
    name = models.CharField(max_length=256, null=True, blank=True)

    def __str__(self):
        return str(self.name)


class ExpenseType(Base):
    name = models.CharField(max_length=256, null=True, blank=True)

    def __str__(self):
        return str(self.name)


class StaffType(Base):
    name = models.CharField(max_length=256, null=True, blank=True)

    def __str__(self):
        return str(self.name)


class VendorType(Base):
    name = models.CharField(max_length=256, null=True, blank=True)

    def __str__(self):
        return str(self.name)


class Customer(Base):
    name = models.CharField(max_length=256, null=True, blank=True)
    phone_number = models.CharField(max_length=256, null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    status = models.CharField(choices=ACTIVITY_STATUS,
                              max_length=255, null=True)

    def __str__(self):
        return str(self.name)


class Inventory(Base):
    item_name = models.CharField(max_length=256, null=True, blank=True)
    item_code = models.CharField(max_length=256, null=True, blank=True)
    manufacturer = models.CharField(max_length=256, null=True, blank=True)
    retail_price = models.FloatField(null=True, blank=True)
    item_tax = models.FloatField(null=True, blank=True)

    def __str__(self):
        return str(self.item_name)


class Billing(Base):
    billDate = models.DateTimeField(
        default=timezone.now, null=True, blank=True)
    item_name = models.ForeignKey(
        Inventory, on_delete=models.CASCADE, related_name='item')
    item_code = models.ForeignKey(
        Inventory, on_delete=models.CASCADE, related_name='code')
    quantity = models.FloatField(null=True, blank=True)
    retail_price = models.ForeignKey(
        Inventory, on_delete=models.CASCADE, related_name='retail')
    item_tax = models.ForeignKey(
        Inventory, on_delete=models.CASCADE, related_name='tax')
    payment_mode = models.ForeignKey(
        PayMode, on_delete=models.CASCADE, related_name='payment')
    customer_name = models.ForeignKey(
        Customer, on_delete=models.CASCADE, related_name='customer_name')
    status = models.CharField(choices=PAYMENT_STATUS,
                              max_length=255, null=True)

    def __str__(self):
        return str(self.item_name)


class Expense(Base):
    expense_type = models.ForeignKey(
        ExpenseType, on_delete=models.CASCADE, related_name='expense_type', null=True, blank=True)
    vendor = models.CharField(max_length=256, null=True, blank=True)
    date_created = models.DateTimeField(
        default=timezone.now, null=True, blank=True)
    amount = models.FloatField(null=True, blank=True)
    payment_mode = models.ForeignKey(
        PayMode, on_delete=models.CASCADE, related_name='payment_mode')
    notes = models.TextField(null=True, blank=True)

    def __str__(self):
        return str(self.vendor)


class Staff(Base):
    name = models.CharField(max_length=256, null=True, blank=True)
    phone_number = models.CharField(max_length=256, null=True, blank=True)
    type = models.ForeignKey(
        StaffType, on_delete=models.CASCADE, related_name='staffType')
    email = models.EmailField(null=True, blank=True)
    status = models.CharField(choices=ACTIVITY_STATUS,
                              max_length=255, null=True)

    def __str__(self):
        return str(self.name)


class Salary(Base):
    staff = models.ForeignKey(Staff, null=True, on_delete=models.CASCADE)
    date = models.DateTimeField(default=timezone.now, null=True, blank=True)
    amount = models.FloatField(null=True, blank=True)
    payment_mode = models.ForeignKey(
        PayMode, on_delete=models.CASCADE, related_name='paymode')
    notes = models.TextField(null=True, blank=True)

    def __str__(self):
        return str(self.staff)


class Vendor(Base):
    name = models.CharField(max_length=256, null=True, blank=True)
    vendor_type = models.ForeignKey(
        VendorType, on_delete=models.CASCADE, related_name='vendor_type')
    phone_number = models.CharField(max_length=256, null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    status = models.CharField(choices=ACTIVITY_STATUS,
                              max_length=255, null=True)

    def __str__(self):
        return str(self.name)
