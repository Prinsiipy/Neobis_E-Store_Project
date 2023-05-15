from django.urls import path

from .views import (
    ProductView,
    ProductDetailView,
    ProductCategoryView,
    ProductCategoryDetailView,
    CommentView,
    CommentDetailView,
)

urlpatterns = [
    path("product", ProductView.as_view(), name="product"),
    path("product/<int:pk>", ProductDetailView.as_view(), name='products'),
    path("product-category", ProductCategoryView.as_view(), name='product-category'),
    path("product-category/<int:pk>", ProductCategoryDetailView.as_view(), name="product-categories"),
    path("comment", CommentView.as_view(), name="comment"),
    path("comment/<int:pk>", CommentDetailView.as_view(), name="comments")
]