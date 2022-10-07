from xml.etree.ElementInclude import include
from django.contrib import admin
from constants import api_version
from django.urls import path, include
from products.views import fetchAllStock, fetchCategories, fetchCategory, fetchRandomProducts, fetchSpecificNumberofDailyDealProducts, fetchSubCategories, fetchSubCategoriesForSpecificCategory, fetchStockForSpecificProduct, fetchDailyDealProducts, lastestProducts, topRatedProducts, trendingItems

from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    #ADMIN
    path('admin/', admin.site.urls),

    #CATEGORIES
    path(api_version + 'fetchCategories/', fetchCategories), 
    path(api_version + 'fetchCategory/<int:id>', fetchCategory),

    # path(version + 'addCategory', addCategory), 
    # path(version + 'addSubCategory', addSubCategory),
    path(api_version + 'fetchSubCategories/', fetchSubCategories),
    path(api_version + 'fetchSubCategory/<int:id>', fetchSubCategoriesForSpecificCategory),
    # path(version + 'addProduct', addProduct),
    # path(version + 'fetchProducts/<int:type>', fetchProducts),

    #PRODUCTS 
    path(api_version + 'fetchDailyProducts/', fetchDailyDealProducts),
    path(api_version + 'fetchSpecificNumberofDailyProducts/', fetchSpecificNumberofDailyDealProducts),
    path(api_version + 'fetchRandomProducts/<int:number_of_items>', fetchRandomProducts),
    path(api_version + 'lastestProducts/<int:number_of_items>', lastestProducts),
    path(api_version + 'trendingItems/<int:number_of_items>', trendingItems),
    path(api_version + 'topRatedProducts/<int:number_of_items>', topRatedProducts),

    #STOCK
    path(api_version + 'fetchAllStock', fetchAllStock),
    path(api_version + 'fetchStockForSpecificProduct/<int:id>', fetchStockForSpecificProduct)
]

# allow response to have various formats
urlpatterns = format_suffix_patterns(urlpatterns)
