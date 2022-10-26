from django.contrib import admin
from ads.models import Ads
from products.models import Categories, ProductStatus, Products, ShowProductAs, SubCategories
from stock.models import Stock
# from users.models import Users

admin.site.register(Categories)
admin.site.register(SubCategories)
admin.site.register(Products)
admin.site.register(Stock)
admin.site.register(ShowProductAs)
admin.site.register(ProductStatus)
admin.site.register(Ads)
# admin.site.register(Users)
