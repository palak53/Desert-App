from django.db import models

class InventoryItem(models.Model):
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    stock_quantity = models.IntegerField()
    needs_reorder = models.BooleanField(default=False)

    def __str__(self):
        return self.name
