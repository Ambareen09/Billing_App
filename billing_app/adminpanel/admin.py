from django.contrib import admin

from adminpanel.models import Billing, Customer, Expense, ExpenseType, Inventory, PayMode, Salary, Staff, StaffType, Vendor, VendorType

# Register your models here.

admin.site.register(Inventory)
admin.site.register(Customer)
admin.site.register(Staff)
admin.site.register(StaffType)
admin.site.register(Vendor)
admin.site.register(Salary)
admin.site.register(Expense)
admin.site.register(ExpenseType)
admin.site.register(Billing)
admin.site.register(VendorType)
admin.site.register(PayMode)
