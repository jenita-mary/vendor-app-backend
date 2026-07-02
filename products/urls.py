from django.urls import path,include
from .views import add_product,  home, product_detail, edit_product,delete_product
from .views import ProductListCreateAPIView, ProductDetailAPIView,ProductViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register(
    'products',
    ProductViewSet,
    basename='product'
)


urlpatterns_old = [
    path('', home, name='home'),

    path(
        'products/<int:product_id>/',
        product_detail,
        name='product_detail'
    ),
    path(
        'products/add/',
        add_product,
        name='add_product'
    ),
    path(
        'products/<int:product_id>/edit/',
        edit_product,
        name='edit_product'
    ),
    path(
        'products/<int:product_id>/delete/',
        delete_product,
        name='delete_product'
    ),

    path(
        'api/products/',
        ProductListCreateAPIView.as_view(),
        name='product_list_create'
    ),

    path(
        'api/products/<int:pk>/',
        ProductDetailAPIView.as_view(),
        name='product_detail'
    ),

    
]

urlpatterns = [
    path(
        'api/',
        include(router.urls),
    ),
]