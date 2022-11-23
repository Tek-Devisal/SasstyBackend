import json
from .models import Categories, Products, SubCategories, SubSubCategories, Vendors
from products.serializers import CategorySerializer, MenuSubCategorySerializer, ProductSerializer, SubCategorySerializer, SubSubCategorySerializer, VendorSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework import status
from random import shuffle

from rest_framework.permissions import AllowAny
from django.db.models import Q

@api_view(['GET'])
@permission_classes([AllowAny])
def search(request, search_query, format=None):
        try:
            products = Products.objects.filter(Q(description__icontains=search_query))
        except Products.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        if request.method  == 'GET':
            serializer = ProductSerializer(products)
            return Response(serializer.data)


@api_view(['GET'])
@permission_classes([AllowAny])
def fetchCategories(request, format=None):
    if request.method == 'GET':
       
        #get all categories
        categories = Categories.objects.all()

        #serialize categories
        serializer = CategorySerializer(categories, many=True)

        #return json
        return Response(serializer.data)


@api_view(['GET'])
@permission_classes([AllowAny])
def fetchCategory(request, id, format=None):
        try:
            category = Categories.objects.get(pk=id)
        except Categories.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        if request.method  == 'GET':
            serializer = CategorySerializer(category)
            return Response(serializer.data)

@api_view(['GET'])
@permission_classes([AllowAny])
def fetchForMenu(request, category_id, format=None):
        try:
            sub_cat = SubCategories.objects.filter(category_id = category_id)
        except SubCategories.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        if request.method  == 'GET':
            serializer = SubCategorySerializer(sub_cat, many=True)

            for subs in range(len(serializer.data)):
                sub_sub_categories = SubSubCategories.objects.filter(sub_category_id = serializer.data[subs]['id'])

                sub_sub_categories_serializer = SubSubCategorySerializer(sub_sub_categories, many=True)
               
                serializer.data[subs]['data'] = sub_sub_categories_serializer.data

            return Response(serializer.data)



# @api_view(['GET'])
# @permission_classes([AllowAny])
# def fetchAllCategories(request, format=None):
#     if request.method == 'GET':

#         res = {}
       
#         #get all categories
#         categories = Categories.objects.all()

#         #serialize categories
#         serializer = CategorySerializer(categories, many=True)

#         # print(serializer)
#         for sub_cats in range(len(serializer.data)):
#             sub_categories = SubCategories.objects.filter(category_id = serializer.data[sub_cats]['id'])

#             sub_categories_serializer = SubCategorySerializer(sub_categories, many=True)

#             for sub_sub in range(len(sub_categories_serializer.data)):
#                 sub_sub_categories = SubSubCategories.objects.filter(sub_category_id = sub_categories_serializer.data[sub_sub]['id'])

#                 sub_sub_categories_serializer = SubSubCategorySerializer(sub_sub_categories, many=True)
#                 sub_categories_serializer.data[sub_sub]['sub_sub'] = sub_sub_categories_serializer.data
#                 # print(sub_sub_categories_serializer.data)
                
#             res[serializer.data[sub_cats]['name']] = sub_categories_serializer.data
#                 # res['data'] = sub_sub_categories_serializer.data

#         #return json
#         return Response(res)


# @api_view(['POST'])
# def addCategory(request, format=None):
#     if request.method == 'POST':

#         serializer = CategorySerializer(data=request.data)

#         if serializer.is_valid():
#             serializer.save()

#             return Response(serializer.data, status=status.HTTP_201_CREATED)


# @api_view(['POST'])
# def addSubCategory(request, format=None):
#      if request.method == 'POST':

#         serializer = SubCategorySerializer(data=request.data)

#         if serializer.is_valid():
#             serializer.save()

#             return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['GET'])
@permission_classes([AllowAny])
def fetchSubCategories(request, format=None):
    if request.method == 'GET':

        #get all sub categories
        sub_categories = SubCategories.objects.all()

        #serialize categories
        serializer = SubCategorySerializer(sub_categories, many=True)

        #return json
        return Response(serializer.data)


@api_view(['GET'])
@permission_classes([AllowAny])
def fetchSubCategoriesForSpecificCategory(request, id, format=None):
        try:
            sub_category = SubCategories.objects.all().filter(category_id=id)
        except SubCategories.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        if request.method  == 'GET':
            serializer = SubCategorySerializer(sub_category, many=True)
            return Response(serializer.data)


@api_view(['GET'])
@permission_classes([AllowAny])
def fetchProductsForSpecificSubSubCategory(request, sub_sub_name, format=None):
        try:
            sub_sub_categorys = SubSubCategories.objects.filter(name = sub_sub_name)
        except SubSubCategories.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        sub_sub_serializer = SubSubCategorySerializer(sub_sub_categorys, many=True)
        if(len(sub_sub_serializer.data) > 0):
            sub_sub_category_products = Products.objects.filter(sub_sub_category_id=sub_sub_serializer.data[0]['id'])

            if request.method  == 'GET':
                serializer = SubCategorySerializer(sub_sub_category_products, many=True)
                return Response(serializer.data)
        else:
            return Response("No such Sub Category")



#PRODUCTS
@api_view(['GET'])
@permission_classes([AllowAny])
def fetchAllProduct(request):
    try:
        products = Products.objects.all()
    except Products.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method  == 'GET':
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)


@api_view(['GET'])
@permission_classes([AllowAny])
def fetchSpecificProduct(request, product_id):
    try:
        products = Products.objects.all().filter(pk=product_id)
    except Products.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method  == 'GET':
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)


@api_view(['GET'])
@permission_classes([AllowAny])
def fetchProductForSpecificCategory(request, sub_category_id):
    try:
        products = Products.objects.all().filter(sub_category_id=sub_category_id)
    except Products.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method  == 'GET':
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)


@api_view(['GET'])
@permission_classes([AllowAny])
def fetchDailyDealProducts(request, format=None):

    try:
        product = Products.objects.all().filter(show_for=1, status = 1).order_by('?')[:4]
    except Products.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method  == 'GET':
        serializer = ProductSerializer(product, many=True)
        return Response(serializer.data)

@api_view(['GET'])
@permission_classes([AllowAny])
def fetchSpecificNumberofDailyDealProducts(request, number_of_items, format=None):
    try:
        product = Products.objects.all().filter(show_for=1, status = 1).order_by('?')[:number_of_items]
    except Products.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method  == 'GET':
        serializer = ProductSerializer(product, many=True)
        return Response(serializer.data)

@api_view(['GET'])
@permission_classes([AllowAny])
def fetchRandomProducts(request, number_of_items, format=None):

    try:
        product = Products.objects.all().filter(status = 1).order_by('?')[:number_of_items]
    except Products.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method  == 'GET':
        serializer = ProductSerializer(product, many=True)
        return Response(serializer.data)

@api_view(['GET'])
@permission_classes([AllowAny])
def lastestProducts(request, number_of_items, format=None):
    try:
        product = Products.objects.all().filter(show_for=2, status = 1).order_by('?')[:number_of_items]
    except Products.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method  == 'GET':
        serializer = ProductSerializer(product, many=True)
        return Response(serializer.data)

@api_view(['GET'])
@permission_classes([AllowAny])
def trendingItems(request, number_of_items, format=None):

    try:
        product = Products.objects.all().filter(show_for=3, status = 1).order_by('?')[:number_of_items]
    except Products.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method  == 'GET':
        serializer = ProductSerializer(product, many=True)
        return Response(serializer.data)

@api_view(['GET'])
@permission_classes([AllowAny])
def topRatedProducts(request, number_of_items, format=None):

    try:
        product = Products.objects.all().filter(show_for=4, status = 1).order_by('?')[:number_of_items]
    except Products.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method  == 'GET':
        serializer = ProductSerializer(product, many=True)
        return Response(serializer.data)

@api_view(['GET'])
@permission_classes([AllowAny])
def fetchAllVendors(request):
    try:
        vendors = Vendors.objects.all().order_by('?')
    except Vendors.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method  == 'GET':
        serializer = VendorSerializer(vendors, many=True)
        return Response(serializer.data)


@api_view(['POST'])
@permission_classes([AllowAny])
def addVendor(request, format=None):
    if request.method == 'POST':

        serializer = VendorSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data, status=status.HTTP_201_CREATED)



# @api_view(['POST'])
# def addProduct(request, format=None):
#     if request.method == 'POST':

#         serializer = ProductSerializer(data=request.data)

#         if serializer.is_valid():
#             serializer.save()

#             return Response(serializer.data, status=status.HTTP_201_CREATED)
