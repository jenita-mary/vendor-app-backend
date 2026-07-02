from django.urls import reverse

from rest_framework import status

from products.models import Product

from .base import BaseProductAPITest


class PaginationTests(BaseProductAPITest):

    def setUp(self):

        self.user, self.vendor = self.create_vendor(
            "vendor1"
        )

        self.authenticate(self.user)

        for i in range(10):

            Product.objects.create(
                vendor=self.vendor,
                name=f"Product {i}",
                description="Test Product",
                price=1000,
                stock=10
            )

    def test_products_are_paginated(self):

        url = reverse("product-list")

        response = self.client.get(url)

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

        self.assertEqual(
            response.data["count"],
            10
        )

        self.assertEqual(
            len(response.data["results"]),
            3
        )