from .models import Categories, Products, Stock, SubCategories
from products.serializers import CategorySerializer, ProductSerializer, StockSerializer, SubCategorySerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response

from rest_framework import status

@api_view(['GET'])
def fetchCategories(request, format=None):
    if request.method == 'GET':

        #get all categories
        categories = Categories.objects.all()

        #serialize categories
        serializer = CategorySerializer(categories, many=True)

        #return json
        return Response(serializer.data)


@api_view(['GET'])
def fetchCategory(request, id, format=None):
        try:
            category = Categories.objects.get(pk=id)
        except Categories.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        if request.method  == 'GET':
            serializer = CategorySerializer(category)
            return Response(serializer.data)


@api_view(['POST'])
def addCategory(request, format=None):
    if request.method == 'POST':

        serializer = CategorySerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['POST'])
def addSubCategory(request, format=None):
     if request.method == 'POST':

        serializer = SubCategorySerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['GET'])
def fetchSubCategories(request, format=None):
    if request.method == 'GET':

        #get all sub categories
        sub_categories = SubCategories.objects.all()

        #serialize categories
        serializer = SubCategorySerializer(sub_categories, many=True)

        #return json
        return Response(serializer.data)


@api_view(['GET'])
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
def fetchProducts(request, type, format=None):
    try:
        product = Products.objects.all().filter(show_for=type)
    except SubCategories.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method  == 'GET':
        serializer = ProductSerializer(product, many=True)
        return Response(serializer.data)


@api_view(['POST'])
def addProduct(request, format=None):
    if request.method == 'POST':

        serializer = ProductSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data, status=status.HTTP_201_CREATED)


#STOCK
@api_view(['POST'])
def addStock(request, format=None):
    if request.method == 'POST':

        serializer = StockSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['GET'])
def fetchAllStock(request, format=None):
    if request.method == 'GET':

        #get all stock
        stock = Stock.objects.all()

        #serialize stock
        serializer = StockSerializer(stock, many=True)

        #return json
        return Response(serializer.data)


@api_view(['GET'])
def fetchStockForSpecificProduct(request, id, format=None):
    try:
        stock = Stock.objects.all().filter(product_id=id)
    except Stock.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method  == 'GET':
        serializer = StockSerializer(stock, many=True)
        return Response(serializer.data)