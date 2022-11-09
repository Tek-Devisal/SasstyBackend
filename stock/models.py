from django.db import models

from products.models import Products

class Stock(models.Model):
    product_id = models.ForeignKey(Products, on_delete=models.CASCADE, null=False, unique = True, related_name='stock')
    quantity = models.IntegerField(null=False)
    # prize = models.IntegerField(null=False, default=0)

    def __str__(self):
        return '{} - {} in stock'.format(self.product_id.name, self.quantity)


