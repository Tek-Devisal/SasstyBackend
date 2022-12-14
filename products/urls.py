from xml.etree.ElementInclude import include
from django.contrib import admin
from constants import api_version
from django.urls import path, include
from products.views import addVendor, fetchAllVendors, fetchCategories, fetchCategory, fetchForMenu, fetchProductForSpecificCategory, fetchProductsForSpecificSubSubCategory, fetchRandomProducts, fetchSpecificNumberofDailyDealProducts, fetchSubCategories, fetchSubCategoriesForSpecificCategory, fetchDailyDealProducts, lastestProducts, search, topRatedProducts, trendingItems, fetchSpecificProduct, fetchAllProduct

from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    #CATEGORIES
    path(api_version + 'fetchCategories/', fetchCategories), 
    path(api_version + 'fetchCategory/<int:id>', fetchCategory),
    # path(api_version + 'fetchAllCategories/', fetchAllCategories),
    path(api_version + 'fetchForMenu/<int:category_id>', fetchForMenu),
    path(api_version + 'fetchProductsForSpecificSubSubCategory/<str:sub_sub_ref_id>', fetchProductsForSpecificSubSubCategory),


    # path(version + 'addCategory', addCategory), 
    # path(version + 'addSubCategory', addSubCategory),
    path(api_version + 'fetchSubCategories/', fetchSubCategories),
    path(api_version + 'fetchSubCategory/<int:id>', fetchSubCategoriesForSpecificCategory),
    # path(api_version + 'addProduct', addProduct),
    path(api_version + 'fetchAllProducts/', fetchAllProduct),

    #SEARCH
    path(api_version + 'search/<str:search_query>', search),

    #PRODUCTS     
    path(api_version + 'fetchSpecificProduct/<int:product_id>', fetchSpecificProduct),
    path(api_version + 'fetchProductForSpecificSubCategory/<int:sub_category_id>', fetchProductForSpecificCategory),
    path(api_version + 'fetchDailyProducts/', fetchDailyDealProducts),
    path(api_version + 'fetchSpecificNumberofDailyProducts/', fetchSpecificNumberofDailyDealProducts),
    path(api_version + 'fetchRandomProducts/<int:number_of_items>', fetchRandomProducts),
    path(api_version + 'lastestProducts/<int:number_of_items>', lastestProducts),
    path(api_version + 'trendingItems/<int:number_of_items>', trendingItems),
    path(api_version + 'topRatedProducts/<int:number_of_items>', topRatedProducts),

    #VENDORS
    path(api_version + 'fetchAllVendors/', fetchAllVendors),
    path(api_version + 'addVendor/', addVendor),

    #FILE UPLOAD
    # path(api_version + 'fileupload/', uploadFile),

]

# allow response to have various formats
urlpatterns = format_suffix_patterns(urlpatterns)
