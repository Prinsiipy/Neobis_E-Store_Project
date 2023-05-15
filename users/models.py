from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=40)
    phone_number = models.CharField(max_length=20, blank=True)
    emai = models.EmailField()
    address = models.CharField(max_length=100, blank=True)


def __str__(self):
    return self.user.username


