from rest_framework import serializers
from .models import Product


class ProductSerializer(serializers.ModelSerializer):

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

    def to_representation(self, instance):
        data = super().to_representation(instance)

        if instance.image:
            data["image"] = instance.image.build_url(secure=True)

        return data