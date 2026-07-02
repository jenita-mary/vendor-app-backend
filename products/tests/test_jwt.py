from django.urls import reverse

from rest_framework import status

from rest_framework_simplejwt.tokens import RefreshToken

from .base import BaseProductAPITest


class JWTTests(BaseProductAPITest):

    def setUp(self):

        self.user, self.vendor = self.create_vendor(
            "vendor1"
        )

    def test_refresh_token_returns_new_access_token(self):

        refresh = RefreshToken.for_user(self.user)

        url = reverse("token_refresh")

        response = self.client.post(
            url,
            {
                "refresh": str(refresh)
            },
            format="json"
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

        self.assertIn(
            "access",
            response.data
        )

    def test_invalid_refresh_token_returns_401(self):

        url = reverse("token_refresh")

        response = self.client.post(
            url,
            {
                "refresh": "invalid_token"
            },
            format="json"
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_401_UNAUTHORIZED
        )