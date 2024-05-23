from .views import ProductListCreate, CategoryListCreate, ProductListByCategory, ProductView, OrderView
from django.urls import path

urlpatterns = [
    path('category/list/', CategoryListCreate.as_view(), name="category"),
    path('category/new/', CategoryListCreate.as_view(), name="create_category"),
    path('products/', ProductListCreate.as_view(), name="product_list"),
    path('products/new/', ProductListCreate.as_view(), name = "create_product"),
    path('products/<int:pk>/', ProductView.as_view(), name="product_details"),
    path('products/category/<int:category>/', ProductListByCategory.as_view(), name="product_list_by_category"),
    path('orders/', OrderView.as_view(), name="all_orders"),
    path('orders/new/',OrderView.as_view(), name="new_order" )
]
