from django.db import models

class ProductEntry(models.Model):
    name = models.CharField(max_length=255)
    price = models.IntegerField()
    description = models.TextField()
    quanity = models.IntegerField()

    @property
    def is_product_available(self):
        return self.quantity > 0