from django.contrib import admin
from .models import Customer, Tag, Product, Order
admin.site.register(Customer)
admin.site.register(Tag)
admin.site.register(Product)
admin.site.register(Order)
