from django.db import models

from users.models import User


class ProductCategory(models.Model):

    name = models.CharField(
        verbose_name="Title",
        max_length=50, unique=True
    )

    def __str__(self):
        return self.name


class Product(models.Model):

    title = models.CharField(verbose_name="Title", max_length=100)
    description = models.TextField(blank=True)
    created_date = models.DateTimeField(auto_now_add=True)
    pictures = models.ImageField(upload_to='images/', blank=True, null=True)
    price = models.FloatField(blank=True, null=True)
    discount = models.DecimalField(
        max_digits=9,
        decimal_places=2,
        default=0
    )
    category = models.ForeignKey(
        ProductCategory,
        related_name="category",
        on_delete=models.CASCADE
    )
    supplier = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return self.title


class Comment(models.Model):

    rates = [
        (1, "1"),
        (2, "2"),
        (3, "3"),
        (4, "4"),
        (5, "5"),
    ]
    rate = models.IntegerField(choices=rates, blank=True, null=True)
    content = models.TextField(blank=True)
    created_date = models.DateTimeField(auto_now_add=True)
    replies = models.ForeignKey(
        "self",
        null=True,
        blank=True,
        on_delete=models.CASCADE
    )
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
    )
    products = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return f"{self.id} {self.user} {self.products}"
