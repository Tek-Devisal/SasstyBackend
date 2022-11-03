from .models import Categories, Products, SubCategories
from products.serializers import CategorySerializer, ProductSerializer, SubCategorySerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework import status
from random import shuffle

from rest_framework.permissions import AllowAny
 
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
    permission_classes = [AllowAny]

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
    permission_classes = [AllowAny]

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
    permission_classes = [AllowAny]

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
    permission_classes = [AllowAny]

    try:
        product = Products.objects.all().filter(show_for=4, status = 1).order_by('?')[:number_of_items]
    except Products.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method  == 'GET':
        serializer = ProductSerializer(product, many=True)
        return Response(serializer.data)


# @api_view(['POST'])
# def addProduct(request, format=None):
#     if request.method == 'POST':

#         serializer = ProductSerializer(data=request.data)

#         if serializer.is_valid():
#             serializer.save()

#             return Response(serializer.data, status=status.HTTP_201_CREATED)
