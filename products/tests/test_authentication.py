from django.urls import reverse

from rest_framework import status

from .base import BaseProductAPITest


class AuthenticationTests(BaseProductAPITest):

    def test_anonymous_user_cannot_access_products(self):

        url = reverse("product-list")

        response = self.client.get(url)

        self.assertEqual(
            response.status_code,
            status.HTTP_401_UNAUTHORIZED
        )