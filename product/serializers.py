from rest_framework import serializers

from .models import (
    Product,
    Comment,
    ProductCategory,
)


class CommentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comment
        fields = [
            'id',
            'rate',
            'content',
            'created_date',
            'replies',
            'user',
            'products',
        ]


class ProductCategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = ProductCategory
        fields = ['id', 'name']


class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = [
            'id',
            'title',
            'description',
            'created_date',
            'pictures',
            'price',
            'discount',
            'category',
            'supplier',
        ]
