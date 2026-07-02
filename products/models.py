from django.db import models
from vendors.models import Vendor
import os


class Product(models.Model):
    vendor = models.ForeignKey(
        Vendor,
        on_delete=models.CASCADE
    )

    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)

    price = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )

    image = models.ImageField(
    upload_to="products/",
    blank=True,
    null=True
    )
    stock = models.PositiveIntegerField(default=0)

    created_at = models.DateTimeField(auto_now_add=True)


    def save(self, *args, **kwargs):

        if self.pk:
            old_product = Product.objects.get(pk=self.pk)

            if (
                old_product.image and
                old_product.image != self.image
            ):
                if os.path.isfile(old_product.image.path):
                    os.remove(old_product.image.path)

        super().save(*args, **kwargs)
        
    def __str__(self):
        return self.name