from django.urls import reverse

from rest_framework import status

from products.models import Product

from .base import BaseProductAPITest


class SearchTests(BaseProductAPITest):

    def setUp(self):

        self.user, self.vendor = self.create_vendor(
            "vendor1"
        )

        self.authenticate(self.user)

        Product.objects.create(
            vendor=self.vendor,
            name="Gaming Mouse",
            description="RGB Mouse",
            price=1500,
            stock=10
        )

        Product.objects.create(
            vendor=self.vendor,
            name="Office Chair",
            description="Comfortable Chair",
            price=5000,
            stock=5
        )

    def test_search_returns_matching_products(self):

        url = reverse("product-list")

        response = self.client.get(
            url,
            {
                "search": "mouse"
            }
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

        self.assertEqual(
            response.data["count"],
            1
        )

        self.assertEqual(
            response.data["results"][0]["name"],
            "Gaming Mouse"
        )