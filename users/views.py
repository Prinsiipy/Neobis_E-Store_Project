from rest_framework.generics import CreateAPIView
from rest_framework.permissions import AllowAny

from .models import User
from .serializers import RegisterUserSerializer
from users.models import Cart


class RegisterAPIView(CreateAPIView):

    serializer_class = RegisterUserSerializer
    permission_classes = (AllowAny,)
    queryset = User.objects.all()


def create_cart(request):
    user = User.objects.get(id=request.user.id)  # Получение текущего пользователя
    cart = Cart(user=user)
    cart.save()
    # ...

