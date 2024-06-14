from django.urls import path
from .views import CategoryListCreateView, CategoryDetailView


urlpatterns = [
    path("category/", CategoryListCreateView.as_view(), name="book_create_List"),
    path("category/<int:pk>/", CategoryDetailView.as_view(), name="category_detail")
]