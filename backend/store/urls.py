from .views import CategoryView
from django.urls import path

urlpatterns = [
    path('category/list/', CategoryView.as_view(), name="category"),
    path('category/new/', CategoryView.as_view(), name="new_category")
    # path('category/list/', category_view, name="categories"),
    # path('product/new/', product_view, name="new_product"),
    # path('all_products/', product_view, name="all_products")
]
