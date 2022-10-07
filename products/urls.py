"""api URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from xml.etree.ElementInclude import include
from django.contrib import admin
from django.urls import path, include
from products.views import fetchAllStock, fetchCategories, fetchCategory, fetchFiveRandomProducts, fetchSubCategories, fetchSubCategoriesForSpecificCategory, fetchStockForSpecificProduct, fetchDailyDealProducts, lastestProducts, trendingItems

from rest_framework.urlpatterns import format_suffix_patterns
version = 'v1/'

urlpatterns = [
    path('admin/', admin.site.urls),
    path(version + 'fetchCategories/', fetchCategories), 
    path(version + 'fetchCategory/<int:id>', fetchCategory),

    # path(version + 'addCategory', addCategory), 
    # path(version + 'addSubCategory', addSubCategory),
    path(version + 'fetchSubCategories/', fetchSubCategories),
    path(version + 'fetchSubCategory/<int:id>', fetchSubCategoriesForSpecificCategory),
    # path(version + 'addProduct', addProduct),
    # path(version + 'fetchProducts/<int:type>', fetchProducts),

    #PRODUCTS 
    path(version + 'fetchDailyProducts/', fetchDailyDealProducts),
    path(version + 'fetchFiveRandomProducts/<int:number_of_items>', fetchFiveRandomProducts),
    path(version + 'lastestProducts/<int:number_of_items>', lastestProducts),
    path(version + 'trendingItems/<int:number_of_items>', trendingItems),

    #STOCK
    path(version + 'fetchAllStock', fetchAllStock),
    path(version + 'fetchStockForSpecificProduct/<int:id>', fetchStockForSpecificProduct)

]

# allow response to have various formats
urlpatterns = format_suffix_patterns(urlpatterns)
