from rest_framework import serializers

from .models import User


class RegisterUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = (
            "username",
            "password",
            "email",
            "first_name",
            "last_name",
            "address",
            "phone",
            "role",
        )
        extra_kwargs = {
            "email": {"required": True},
            "username": {"required": True},
            "first_name": {"required": True},
            "last_name": {"required": True},
            "password": {"write_only": True},
        }

    def create(self, validated_data):
        user = User.objects.create(
            username=validated_data["username"],
            email=validated_data["email"],
            first_name=validated_data["first_name"],
            last_name=validated_data["last_name"],
            address=validated_data["address"],
            phone=validated_data["phone"],
        )

        user.set_password(validated_data["password"])
        user.save()

        return user
