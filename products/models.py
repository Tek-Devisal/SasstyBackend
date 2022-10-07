from email.policy import default
from django.db import models
from django.contrib import admin

class Categories(models.Model):
    # id = models.BigAutoField(max_length=10, primary_key=True)
    # ref = models.CharField(max_length=10,default=generate_id(8, "ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"))
    name = models.CharField(max_length=500, null=False)

    def __str__(self):
        return self.name
    
class SubCategories(models.Model):
    # category_id = models.IntegerField(null=False)
    category_id = models.ForeignKey(Categories, on_delete=models.CASCADE, null=False)
    name = models.CharField(max_length=500, null=False)

    def __str__(self):
        return self.name

class ProductStatus(models.Model):
    name = models.CharField(max_length=500, null=False)

    def __str__(self):
        return '{} - {}'.format(self.pk, self.name)

class ShowProductAs(models.Model):
    name = models.CharField(max_length=500, null=False)

    def __str__(self):
        return '{} - {}'.format(self.pk, self.name)

class Products(models.Model):
    vendor_id = models.IntegerField(null=False)
    # vendor_id = models.ForeignKey(Categories, on_delete=models.CASCADE, null=False)
    # show_for = models.IntegerField(null=False)
    show_for = models.ForeignKey(ShowProductAs, on_delete=models.CASCADE, null=False)
    status = models.ForeignKey(ProductStatus, on_delete=models.CASCADE, null=False)
    category_id = models.ForeignKey(Categories, on_delete=models.CASCADE, null=False)
    sub_category_id =  models.ForeignKey(SubCategories, on_delete=models.CASCADE, null=False)
    name = models.CharField(max_length=500, null=False)
    description = models.CharField(max_length=1000, null=False)
    prize = models.FloatField(max_length=50, null=False)
    discount = models.IntegerField(null=False)
    img_1 = models.ImageField(blank=False, default="", upload_to="../images/products/")
    img_2 = models.ImageField(blank=True, default="", upload_to="../images/products/")
    img_3 = models.ImageField(blank=True, default="", upload_to="../images/products/")

    def __str__(self):
        return '{} - {}'.format(self.pk, self.name)

class Stock(models.Model):
    product_id = models.ForeignKey(Products, on_delete=models.CASCADE, null=False)
    quantity = models.IntegerField(null=False)
    prize = models.IntegerField(null=False, default=0)

    def __str__(self):
        return self.product_id



