
from xml.etree.ElementInclude import include
from django.contrib import admin
from django.urls import path, include
from drf_yasg import openapi
from rest_framework import permissions
from drf_yasg.views import get_schema_view as swagger_get_schema_view
from django.conf import settings
from django.conf.urls.static import static


schema_view = swagger_get_schema_view(
    openapi.Info(
        title="Posts API",
        default_version='1.0.0',
        description="API documentation of App",
    ),
    public=True,
)

urlpatterns = [
    path('admin/doc/', include('django.contrib.admindocs.urls')),

    path('admin/', admin.site.urls),
    path('products/', include('products.urls')),
    path('ads/', include('ads.urls')),
    path('stock/', include('stock.urls')),
    path('users/', include('users.urls')),
    path('cart/', include('cart.urls')),
    path('orders/', include('orders.urls')),

    # path('docs/', include_docs_urls(title="Sassty API documentation")),
    # path('docs/', schema_view)
    path('docs/', schema_view.with_ui('swagger', cache_timeout=0), name="swagger-schema",),
]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

