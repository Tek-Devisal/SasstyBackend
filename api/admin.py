from django.contrib import admin
from products.models import Categories, Products, Stock, SubCategories

admin.site.register(Categories)
admin.site.register(SubCategories)
admin.site.register(Products)
admin.site.register(Stock)