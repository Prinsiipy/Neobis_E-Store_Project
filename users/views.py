from rest_framework.generics import CreateAPIView
from rest_framework.permissions import AllowAny

from .models import User
from .serializers import RegisterUserSerializer


class RegisterAPIView(CreateAPIView):

    serializer_class = RegisterUserSerializer
    permission_classes = (AllowAny,)
    queryset = User.objects.all()


