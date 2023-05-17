from django.contrib.auth.base_user import AbstractBaseUser
from django.db import models
from django.contrib.auth.models import Group, Permission, PermissionsMixin


class User(AbstractBaseUser, PermissionsMixin):

    groups = models.ManyToManyField(
        Group,
        verbose_name='groups',
        blank=True,
        related_name='user_groups'  # Измененный related_name
    )
    user_permissions = models.ManyToManyField(
        Permission,
        verbose_name='user permissions',
        blank=True,
        related_name='user_permissions'  # Измененный related_name
    )


class Cart(models.Model):

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='cart_user'  # Измененный related_name
    )
