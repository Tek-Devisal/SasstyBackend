from xml.etree.ElementInclude import include
from django.contrib import admin
from constants import api_version
from django.urls import path, include
from stock.views import fetchAllStock, fetchStockForSpecificProduct

from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    #ADMIN
    path('admin/', admin.site.urls),

    #STOCK
    path(api_version + 'fetchAllStock', fetchAllStock),
    path(api_version + 'fetchStockForSpecificProduct/<int:id>', fetchStockForSpecificProduct)
]

# allow response to have various formats
urlpatterns = format_suffix_patterns(urlpatterns)
