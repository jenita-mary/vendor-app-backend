from django.urls import reverse

from rest_framework import status

from products.models import Product

from .base import BaseProductAPITest


class ProductTests(BaseProductAPITest):

    def setUp(self):

        self.user, self.vendor = self.create_vendor(
            "vendor1"
        )

        self.authenticate(self.user)

    def test_vendor_can_create_product(self):

        url = reverse("product-list")

        response = self.client.post(
            url,
            {
                "name": "Gaming Mouse",
                "description": "RGB Mouse",
                "price": "1500.00",
                "stock": 10,
            }
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_201_CREATED
        )

        self.assertEqual(
            Product.objects.count(),
            1
        )

        product = Product.objects.first()

        self.assertEqual(
            product.vendor,
            self.vendor
        )

    def test_vendor_can_delete_own_product(self):

        product = Product.objects.create(
            vendor=self.vendor,
            name="Gaming Mouse",
            description="RGB Mouse",
            price=1500,
            stock=10
        )

        url = reverse(
            "product-detail",
            args=[product.id]
        )

        response = self.client.delete(url)

        self.assertEqual(
            response.status_code,
            status.HTTP_204_NO_CONTENT
        )

        self.assertEqual(
            Product.objects.count(),
            0
        )   

    def test_vendor_can_update_own_product(self):

        product = Product.objects.create(
            vendor=self.vendor,
            name="Gaming Mouse",
            description="RGB Mouse",
            price=1500,
            stock=10
        )

        url = reverse(
            "product-detail",
            args=[product.id]
        )

        response = self.client.patch(
            url,
            {
                "price": 3000
            },
            format="json"
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

        product.refresh_from_db()

        self.assertEqual(
            product.price,
            3000
        )             