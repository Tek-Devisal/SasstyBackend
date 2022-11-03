from django.contrib import admin
from ads.models import Ads
from cart.models import Cart
from products.models import Categories, ProductStatus, Products, ShowProductAs, SubCategories
from stock.models import Stock
from orders.models import DeliveryAddress, Ghanaian_Regions, Orders

# from users.models import Users

admin.site.register(Categories)
admin.site.register(SubCategories)
admin.site.register(Products)
admin.site.register(Stock)
admin.site.register(ShowProductAs)
admin.site.register(ProductStatus)
admin.site.register(Ads)
admin.site.register(Cart)
admin.site.register(DeliveryAddress)
admin.site.register(Ghanaian_Regions)
admin.site.register(Orders)

# admin.site.register(Users)
