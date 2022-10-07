from django.contrib import admin
from products.models import Categories, ProductStatus, Products, ShowProductAs, Stock, SubCategories

admin.site.register(Categories)
admin.site.register(SubCategories)
admin.site.register(Products)
admin.site.register(Stock)
admin.site.register(ShowProductAs)
admin.site.register(ProductStatus)
