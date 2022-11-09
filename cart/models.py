from django.db import models
from products.models import Products

from users.models import User

class Cart(models.Model):
    product_id = models.ForeignKey(Products, on_delete=models.CASCADE, null=False)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, null=False)
    quantity = models.IntegerField(null=False)
    prize = models.IntegerField(null=False, default=0)
    total_amount = models.IntegerField(null=False, default=0)

    def __str__(self):
        return '{} - ({}) {} in cart'.format(self.user_id, self.quantity, self.product_id.name)

    class Meta:
        verbose_name = "Cart"
        verbose_name_plural = "Cart"

