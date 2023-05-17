from django.urls import path

from .views import (
    CartView,
    CartDetailView,
    CartItemView,
    CartItemDetailView,
    OrderView,
    OrderDetailView,
)

urlpatterns = [
    path("cart", CartView.as_view(), name="cart"),
    path("cart/<int:pk>", CartDetailView.as_view(), name="carts"),
    path("cart-item", CartItemView.as_view(), name="cart-item"),
    path("cart-item/<int:pk>", CartItemDetailView.as_view(), name="cart-items"),
    path("order", OrderView.as_view(), name="order"),
    path("order/<int:pk>", OrderDetailView.as_view(), name="orders"),
]