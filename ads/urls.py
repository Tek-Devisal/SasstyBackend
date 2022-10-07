from sys import api_version
from xml.etree.ElementInclude import include
from django.contrib import admin
from django.urls import path, include
from ads.views import fetchAds
from constants import api_version

from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    #ADMIN
    path('admin/', admin.site.urls),

    path(api_version + 'fetchAds/<int:number_of_ads>', fetchAds), 
]

# allow response to have various formats
urlpatterns = format_suffix_patterns(urlpatterns)
