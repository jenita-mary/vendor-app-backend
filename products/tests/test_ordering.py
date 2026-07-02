from django.urls import reverse

from rest_framework import status

from products.models import Product

from .base import BaseProductAPITest


class OrderingTests(BaseProductAPITest):

    def setUp(self):

        self.user, self.vendor = self.create_vendor(
            "vendor1"
        )

        self.authenticate(self.user)

        Product.objects.create(
            vendor=self.vendor,
            name="Laptop",
            description="Highend Laptop",
            price=65000,
            stock=10
        )

        Product.objects.create(
            vendor=self.vendor,
            name="Mouse",
            description="RGB Mouse",
            price=1500,
            stock=5
        )

        Product.objects.create(
            vendor=self.vendor,
            name="Keyboard",
            description="Mechanical Keyboard",
            price=4500,
            stock=5
        )        

    def test_ordering_returns_products_in_correct_order(self):

        url = reverse("product-list")

        response = self.client.get(
            url,
            {
                "ordering": "-price"
            }
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )


        self.assertEqual(
            response.data["results"][0]["name"],
            "Laptop"
        )   

        self.assertEqual(
            response.data["results"][1]["name"],
            "Keyboard"
        )

        self.assertEqual(
            response.data["results"][2]["name"],
            "Mouse"
        )     