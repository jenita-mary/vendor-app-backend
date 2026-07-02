from rest_framework.test import APITestCase
from rest_framework_simplejwt.tokens import RefreshToken

from accounts.models import User
from vendors.models import Vendor


class BaseProductAPITest(APITestCase):

    def create_vendor(
        self,
        username,
        company_name="ABC Pvt Ltd"
    ):

        user = User.objects.create_user(
            username=username,
            password="Test@123",
            role="vendor"
        )

        vendor = Vendor.objects.create(
            user=user,
            company_name=company_name,
            phone="9876543210"
        )

        return user, vendor

    def authenticate(self, user):

        refresh = RefreshToken.for_user(user)

        access = str(refresh.access_token)

        self.client.credentials(
            HTTP_AUTHORIZATION=f"Bearer {access}"
        )