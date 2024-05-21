from django.contrib import admin
from .models import *

# Register your models here.


class StoreAdmin(admin.ModelAdmin):
    list_display = ["name", "date"]
    list_filter = ["name"]
    search_fields = ["name"]


admin.site.register(Product, StoreAdmin)
admin.site.register(Customer)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(DeliveryAddress)
