from django.db import models
from django.db import models
from django.contrib.auth.models import User

class InventoryItem(models.Model):
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    stock_quantity = models.IntegerField()
    needs_reorder = models.BooleanField(default=False)

    def __str__(self):
        return self.name

class Notification(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    message = models.CharField(max_length=255)
    is_read = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.message
