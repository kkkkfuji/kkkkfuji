from django.contrib import admin

from .models import Customer, Customer_category, Order

# Register your models here.

admin.site.register(Customer)
admin.site.register(Customer_category)
admin.site.register(Order)


