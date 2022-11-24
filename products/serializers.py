from rest_framework import serializers

from stock.models import Stock
from stock.serializers import StockSerializer
from .models import Categories, ProductStatus, Products, ShowProductAs, SubCategories, ProductStatus, SubSubCategories, Vendors

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Categories
        fields = ['id', 'name']

class SubCategorySerializer(serializers.ModelSerializer):
    class Meta: 
        model = SubCategories
        fields = ['id', 'name']

class MenuSubCategorySerializer(serializers.ModelSerializer):
    class Meta: 
        model = SubCategories
        fields = ['name']

class SubSubCategorySerializer(serializers.ModelSerializer):
    sub_category_id_ = SubCategorySerializer(many=True, read_only=True)

    class Meta: 
        model = SubSubCategories
        fields = ['id', 'sub_category_id_', 'ref_code', 'name']

class StatusSerializer(serializers.ModelSerializer):
    class Meta: 
        model = ProductStatus
        fields = ['id', 'name']

class ShowProductAsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShowProductAs
        fields = ['id', 'name']

class VendorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vendors
        fields = ['id', 'shop_name', 'manager_name', 'phone_number', 'location', 'ghana_card']

class ProductSerializer(serializers.ModelSerializer):
    stock = StockSerializer(many=True, read_only=True)
    # print(stock)
    class Meta:
        model = Products
        fields = ['id', 'vendor_id', 'show_for', 'status', 'category_id', 'sub_category_id', 'sub_sub_category_id', 'name', 'description', 'prize', 'discount', 'img_1', 'img_2', 'img_3', 'img_4', 'img_5', 'img_6','stock']
        
