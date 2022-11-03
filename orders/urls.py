from xml.etree.ElementInclude import include
from django.contrib import admin
from constants import api_version
from django.urls import path, include
from orders.views import addDeliveryAddress, fetchAllDeliveryAddressesPerUser,updateDeliveryAddress,removeDeliveryAddress, setDeliveryAddressAsPrimary, addNewOrder, fetchAllOrders
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path(api_version + 'addDeliveryAddress/', addDeliveryAddress), 
    path(api_version + 'fetchDeliveryAddressPerUser/<int:user_id>', fetchAllDeliveryAddressesPerUser),
    path(api_version + 'updateDeliveryAddress/<int:id>', updateDeliveryAddress),
    path(api_version + 'removeDeliveryAddress/<int:id>', removeDeliveryAddress),
    path(api_version + 'setDeliveryAddressAsPrimary/<int:id>', setDeliveryAddressAsPrimary),

    #ORDERS
    path(api_version + 'addNewOrder/<int:user_id>', addNewOrder),
    path(api_version + 'fetchAllOrders/', fetchAllOrders),

]

# allow response to have various formats
urlpatterns = format_suffix_patterns(urlpatterns)
