from django.contrib import admin
from .models import Product, Category, Website


admin.site.register(Product)
admin.site.register(Website)
admin.site.register(Category)

