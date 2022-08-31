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


# Create your models here.
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


class StaffType(Base):
    name = models.CharField(max_length=256, null=True, blank=True)

    def __str__(self):
        return str(self.name)


class VendorType(Base):
    name = models.CharField(max_length=256, null=True, blank=True)

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
        User, on_delete=models.CASCADE, related_name='name')

    def __str__(self):
        return str(self.item_name)


class Expense(Base):
    expense_type = models.CharField(max_length=256, null=True, blank=True)
    vendor = models.CharField(max_length=256, null=True, blank=True)
    date_created = models.DateTimeField(null=True, blank=True)
    amount = models.FloatField(null=True, blank=True)
    payment_mode = models.ForeignKey(
        PayMode, on_delete=models.CASCADE, related_name='payment_mode')
    notes = models.TextField(null=True, blank=True)

    def __str__(self):
        return str(self.vendor)


class Salary(Base):
    staff = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='staff')
    # staff_type = models.ForeignKey(User, related_name='staff_type')
    date = models.DateTimeField(null=True, blank=True)
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

    def __str__(self):
        return str(self.name)


class Staff(Base):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, related_name='staff_name')
    type = models.ForeignKey(
        StaffType, on_delete=models.CASCADE, related_name='staffType')
    email = models.EmailField(null=True, blank=True)

    def __str__(self):
        return str(self.user)


class Customer(Base):
    name = models.CharField(max_length=256, null=True, blank=True)
    phone_number = models.CharField(max_length=256, null=True, blank=True)
    email = models.EmailField(null=True, blank=True)

    def __str__(self):
        return str(self.name)
