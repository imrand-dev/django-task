import uuid
from django.db import models


class Customer(models.Model):
    uid = models.UUIDField(
        unique=True, 
        default=uuid.uuid4,
        editable=False, 
        db_index=True
    )
    name = models.CharField(max_length=255)
    phone = models.CharField(max_length=15, unique=True)
    email = models.EmailField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
