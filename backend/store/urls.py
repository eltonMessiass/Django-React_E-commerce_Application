from .views import CategoryView, ProductView, ProductListCreate, CategoryListCreate, ProductListByCategory
from django.urls import path

urlpatterns = [
    path('category/list/', CategoryListCreate.as_view(), name="category"),
    path('category/new/', CategoryListCreate.as_view(), name="create_category"),
    path('category/<int:category>/products/', ProductView().as_view(), name="products_by_category"),
    path('products/list/', ProductListCreate.as_view(), name="product_list"),
    path('product/new/', ProductListCreate.as_view(), name = "create_product"),
    path('products/category/<int:category>/', ProductListByCategory.as_view(), name="product_list_by_category")
    # path('category/list/', category_view, name="categories"),
    # path('product/new/', product_view, name="new_product"),
    # path('all_products/', product_view, name="all_products")
]
