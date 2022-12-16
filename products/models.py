from email.policy import default
from enum import unique
from tabnanny import verbose
from django.db import models
from django.contrib import admin

from functions import generate_id

class Categories(models.Model):
    # id = models.BigAutoField(max_length=10, primary_key=True)
    # ref = models.CharField(max_length=10,default=generate_id(8, "ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"))
    name = models.CharField(max_length=500, null=False)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"

    
class SubCategories(models.Model):
    # category_id = models.IntegerField(null=False)
    category_id = models.ForeignKey(Categories, on_delete=models.CASCADE, null=False)
    name = models.CharField(max_length=500, null=False)

    def __str__(self):
        return self.name
    class Meta:
        verbose_name = "Sub Category"
        verbose_name_plural = "Sub Categories"

class SubSubCategories(models.Model):
    # category_id = models.IntegerField(null=False)
    sub_category_id = models.ForeignKey(SubCategories, on_delete=models.CASCADE, null=False)
    ref_code = models.CharField(max_length=500, default=generate_id(8))
    name = models.CharField(max_length=500, null=False)

    def __str__(self):
        return self.name
    class Meta:
        verbose_name = "Sub Sub Category"
        verbose_name_plural = "Sub Sub Categories"


class ProductStatus(models.Model):
    name = models.CharField(max_length=500, null=False)

    def __str__(self):
        return '{} - {}'.format(self.pk, self.name)
    class Meta:
        verbose_name = "Product Status"
        verbose_name_plural = "Product Status"

class ShowProductAs(models.Model):
    name = models.CharField(max_length=500, null=False)

    def __str__(self):
        return '{} - {}'.format(self.pk, self.name)

    class Meta:
        verbose_name = "Show Product As"
        verbose_name_plural = "Show Products As"
class Vendors(models.Model):
    shop_name = models.CharField(max_length=500, null=False)
    manager_name = models.CharField(max_length=500, null=False)
    phone_number = models.CharField(max_length=500, null=False)
    location = models.CharField(max_length=500, null=False)
    ghana_card = models.FileField(blank=False, default="", upload_to="documents/vendors/ghanacard")

    def __str__(self):
        return '{} - {}'.format(self.shop_name, self.location)

    class Meta:
        verbose_name = "Vendor"
        verbose_name_plural = "Vendors"

class Products(models.Model):
    # vendor_id = models.IntegerField(null=False)
    vendor_id = models.ForeignKey(Vendors, on_delete=models.CASCADE, null=False, default=0)
    # show_for = models.IntegerField(null=False)
    show_for = models.ForeignKey(ShowProductAs, on_delete=models.CASCADE, null=False)
    status = models.ForeignKey(ProductStatus, on_delete=models.CASCADE, null=False, default = 0)
    category_id = models.ForeignKey(Categories, on_delete=models.CASCADE, null=False)
    sub_category_id =  models.ForeignKey(SubCategories, on_delete=models.CASCADE, null=False)
    sub_sub_category_id = models.ForeignKey(SubSubCategories, on_delete=models.CASCADE, null=False, default = 0)
    name = models.CharField(max_length=500, null=False)
    description = models.CharField(max_length=1000, null=False)
    prize = models.FloatField(max_length=50, null=False)
    discount = models.IntegerField(null=False)
    # img_1 = models.ImageField(blank=False, default="",upload_to="https://storage.googleapis.com/sassty-5b85e.appspot.com/images/")
    img_1 = models.ImageField(blank=False, default="",upload_to="images/products/")
    img_2 = models.ImageField(blank=True, default="", upload_to="images/products/")
    img_3 = models.ImageField(blank=True, default="", upload_to="images/products/")
    img_4 = models.ImageField(blank=True, default="", upload_to="images/products/")
    img_5 = models.ImageField(blank=True, default="", upload_to="images/products/")
    img_6 = models.ImageField(blank=True, default="", upload_to="images/products/")


    def __str__(self):
        return '{} - {}'.format(self.pk, self.name)

    class Meta:
        verbose_name = "Product"
        verbose_name_plural = "Products"
