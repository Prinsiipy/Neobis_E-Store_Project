from rest_framework import generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.response import Response

from .serializers import (
    CartSerializer,
    CartItemSerializer,
    OrderSerializer
)
from .models import Cart, CartItem, Order
from .permissions import IsOwner, IsSupplierOrReadOnly


class CartItemView(generics.ListCreateAPIView):
    serializer_class = CartItemSerializer
    permission_classes = (IsSupplierOrReadOnly,)
    queryset = CartItem.objects.all()


class CartItemDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = CartItemSerializer
    permission_classes = (IsSupplierOrReadOnly,)
    queryset = CartItem.objects.all()


class CartView(generics.ListCreateAPIView):
    serializer_class = CartSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)

    def get_queryset(self):
        return Cart.objects.filter(is_order=False, user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class CartDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = CartSerializer
    permission_classes = (IsOwner,)
    queryset = Cart.objects.all()


class OrderView(generics.ListCreateAPIView):
    serializer_class = OrderSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)

    def get_queryset(self):
        return Order.objects.filter(user=self.request.user)

    def post(self, request, *args, **kwargs):
        serializer = OrderSerializer(data=request.data)
        if serializer.is_valid():
            cart = serializer.validated_data['cart']
            cart.is_order = True
            cart.save()
            serializer.save(user=self.request.user)
            return Response(serializer.data)
        return Response(serializer.errors)


class OrderDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = OrderSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)
    queryset = Order.objects.all()
