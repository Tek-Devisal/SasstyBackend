from django.contrib import admin
from ads.models import Ads
from cart.models import Cart
from products.models import Categories, ProductStatus, Products, ShowProductAs, SubCategories, Vendors
from stock.models import Stock
from orders.models import DeliveryAddress, Ghanaian_Regions, OrderProducts, Orders

# from users.models import Users

admin.site.register(Categories)
admin.site.register(SubCategories)
admin.site.register(Products)
admin.site.register(Stock)
admin.site.register(ShowProductAs)
admin.site.register(ProductStatus)
admin.site.register(Vendors)
admin.site.register(Ads)
admin.site.register(Cart)
admin.site.register(DeliveryAddress)
admin.site.register(Ghanaian_Regions)
admin.site.register(Orders)
admin.site.register(OrderProducts)


# admin.site.register(Users)
