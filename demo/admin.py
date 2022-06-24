from django.contrib import admin

from demo.forms import OrderForm
from demo.models import *


# Register your models here.


class ProductOrder(admin.TabularInline):
    model = ProductOrder


class OrderAdmin(admin.ModelAdmin):
    form = OrderForm
    list_filter = ('status',)
    list_display = ('date', 'user', 'count_product')
    fields = ('status', 'rejection_reason')
    inlines = (ProductOrder,)


admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Order, OrderAdmin)
