from django.db import models
from products.models import Products

from users.models import User

class Ghanaian_Regions(models.Model):
    name = models.CharField(max_length=500, null=False)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Regions"
        verbose_name_plural = "Regions"


class DeliveryAddress(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, null=False)
    is_primary = models.BooleanField(null=False, default=False)
    street_name = models.CharField(max_length=500, null=False)
    town  = models.CharField(max_length=500, null=False)
    district = models.CharField(max_length=500, null=False)
    region = models.ForeignKey(Ghanaian_Regions, on_delete=models.CASCADE, null=False)

    def __str__(self):
        return '{} - {},{},{}'.format(self.user_id, self.street_name, self.town, self.region)

    class Meta:
        verbose_name = "Delivery Address"
        verbose_name_plural = "Delivery Addresses"


class Orders(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, null=False)
    status = models.IntegerField(null=False, default=0)
    payment_status = models.IntegerField(null=False, default=0)
    order_code = models.CharField(max_length=500, null=False)

    def __str__(self):
            if self.payment_status == 0:
                has_paid = "Pending"
            else: has_paid = "Paid"
            return '{} - {}: {}'.format(self.user_id, self.order_code, has_paid)

    class Meta:
        verbose_name = "Order"
        verbose_name_plural = "Orders"


class OrderProducts(models.Model):
    order_code = models.CharField(max_length=500, null=False)
    delivery_address_id = models.ForeignKey(DeliveryAddress, on_delete=models.CASCADE, null=False)
    product_id = models.ForeignKey(Products, on_delete=models.CASCADE, null=False)
    quantity = models.IntegerField(null=False)
    prize = models.IntegerField(null=False, default=0)
    total_amount = models.IntegerField(null=False, default=0)

    def __str__(self):
        return '{} - {}'.format(self.order_code, self.product_id)

    class Meta:
        verbose_name = "Products Ordered"
        verbose_name_plural = "Products Ordered"


