from rest_framework import generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from .serializers import (
    ProductCategorySerializer,
    CommentSerializer,
    ProductSerializer
)
from .models import (
    ProductCategory,
    Comment,
    Product,
)
from cart.permissions import IsSupplierOrReadOnly


class ProductCategoryView(generics.ListCreateAPIView):
    serializer_class = ProductCategorySerializer
    permission_classes = (IsSupplierOrReadOnly,)
    queryset = ProductCategory.objects.all()


class ProductCategoryDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ProductCategorySerializer
    permission_classes = (IsSupplierOrReadOnly,)
    queryset = ProductCategory.objects.all()


class ProductView(generics.ListCreateAPIView):
    serializer_class = ProductSerializer
    permission_classes = (IsSupplierOrReadOnly,)
    queryset = Product.objects.all()


class ProductDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ProductSerializer
    permission_classes = (IsSupplierOrReadOnly,)
    queryset = Product.objects.all()


class CommentView(generics.ListCreateAPIView):
    serializer_class = CommentSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)
    queryset = Comment.objects.all()


class CommentDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = CommentSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)
    queryset = Comment.objects.all()
