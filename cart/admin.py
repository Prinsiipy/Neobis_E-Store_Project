from django.contrib import admin
from .models import CartItem, Cart, Order

admin.site.register(Cart)
admin.site.register(CartItem)
admin.site.register(Order)