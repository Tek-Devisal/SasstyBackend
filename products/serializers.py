from dataclasses import field
from rest_framework import serializers
from .models import Categories, ProductStatus, Products, ShowProductAs, Stock, SubCategories, ProductStatus

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Categories
        fields = ['id', 'name']


class SubCategorySerializer(serializers.ModelSerializer):
    class Meta: 
        model = SubCategories
        fields = ['id', 'category_id', 'name']

class StatusSerializer(serializers.ModelSerializer):
    class Meta: 
        model = ProductStatus
        fields = ['id', 'name']


class ShowProductAsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShowProductAs
        fields = ['id', 'name']

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Products
        fields = ['id', 'vendor_id', 'show_for', 'status', 'category_id', 'sub_category_id', 'name', 'description', 'prize', 'discount', 'img_1', 'img_2', 'img_3']

class StockSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stock
        fields = ['id', 'product_id', 'quantity']