from django.urls import reverse
from django.core.files.uploadedfile import SimpleUploadedFile

from rest_framework import status

from products.models import Product

from .base import BaseProductAPITest


class ImageUploadTests(BaseProductAPITest):

    def setUp(self):

        self.user, self.vendor = self.create_vendor(
            "vendor1"
        )

        self.authenticate(self.user)

    def test_vendor_can_upload_product_image(self):

        from io import BytesIO
        from PIL import Image

        image_io = BytesIO()

        image = Image.new(
            "RGB",
            (100, 100),
            color="red"
        )

        image.save(
            image_io,
            format="JPEG"
        )

        image_io.seek(0)

        uploaded_image = SimpleUploadedFile(
            "test.jpg",
            image_io.read(),
            content_type="image/jpeg"
        )

        url = reverse("product-list")

        response = self.client.post(
            url,
            {
                "name": "Gaming Mouse",
                "description": "RGB Mouse",
                "price": "1500.00",
                "stock": 10,
                "image": uploaded_image,
            },
            format="multipart"
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

        self.assertTrue(
            bool(product.image)
        )