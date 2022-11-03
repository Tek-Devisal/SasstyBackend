from cart.views import addToCart
from constants import api_version
from django.urls import path

from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path(api_version + 'addToCart/', addToCart), 
]

# allow response to have various formats
urlpatterns = format_suffix_patterns(urlpatterns)
