from rest_framework.routers import DefaultRouter
from constants import api_version

from django.contrib import admin
from django.urls import path, include
from rest_framework.urlpatterns import format_suffix_patterns

# from users.views import RegisterAPI
from rest_framework_simplejwt.views import (
TokenObtainPairView,
TokenRefreshView,
)

from users.views import Register, fetchAllUsers

urlpatterns = [
    #LOGIN
    path(api_version + 'api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path(api_version + 'api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path(api_version + 'register', Register.as_view(), name='register'),
    path(api_version + 'fetchAllUsers', fetchAllUsers, name='fetchAllUsers'),

]

# allow response to have various formats
urlpatterns = format_suffix_patterns(urlpatterns)