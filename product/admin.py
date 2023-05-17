from django.contrib import admin
from .models import Product, ProductCategory, Comment

admin.site.register(Product)
admin.site.register(ProductCategory)
admin.site.register(Comment)