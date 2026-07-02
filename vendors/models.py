from django.db import models
from django.conf import settings


class Vendor(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='vendor_profile'
    )
    company_name = models.CharField(max_length=255)
    phone = models.CharField(max_length=20)
    
    address = models.TextField(
        blank=True,
        null=True
    )


    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.company_name