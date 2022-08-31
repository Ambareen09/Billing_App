from django.contrib import admin

from adminpanel.models import Billing, Customer, Expense, PayMode, Salary, Staff, Vendor, VendorType

# Register your models here.

admin.site.register(Customer)
admin.site.register(Staff)
admin.site.register(Vendor)
admin.site.register(Salary)
admin.site.register(Expense)
admin.site.register(Billing)
admin.site.register(VendorType)
admin.site.register(PayMode)
