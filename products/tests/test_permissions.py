from django.urls import reverse

from rest_framework import status
from products.models import Product

from .base import BaseProductAPITest


class PermissionTests(BaseProductAPITest):

    def setUp(self):

        self.user1, self.vendor1 = self.create_vendor(
            "vendor1"
        )

        self.user2, self.vendor2 = self.create_vendor(
            "vendor2"
        )

        self.product = Product.objects.create(
            vendor=self.vendor1,
            name="Gaming Mouse",
            description="RGB Mouse",
            price=1500,
            stock=10
        )

    def test_vendor_cannot_update_other_vendor_product(self):

        self.authenticate(self.user2)

        url = reverse(
            "product-detail",
            args=[self.product.id]
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
            status.HTTP_404_NOT_FOUND
        )

    def test_vendor_cannot_delete_other_vendor_product(self):

        # Authenticate as Vendor 2
        self.authenticate(self.user2)

        url = reverse(
            "product-detail",
            args=[self.product.id]
        )

        response = self.client.delete(url)

        self.assertEqual(
            response.status_code,
            status.HTTP_404_NOT_FOUND
        )

        # Product should still exist
        self.assertEqual(
            Product.objects.count(),
            1
        )