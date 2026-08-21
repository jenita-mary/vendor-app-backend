# products/serializers.py

from rest_framework import serializers
from .models import Product


class ProductSerializer(serializers.ModelSerializer):

    image = serializers.SerializerMethodField()
    class Meta:
        model = Product
        fields = [
            'id',
            'name',
            'description',
            'price',
            'stock',
            'image',
            'created_at',
        ]

    def get_image(self, obj):
        if not obj.image:
            return None

        return obj.image.build_url(secure=True)