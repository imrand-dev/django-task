import uuid
from django.db import models
from django.contrib.auth.models import User


class Employee(models.Model):
    ROLE = (
        ("Admin", "Admin"),
        ("Medicine Manager", "Medicine Manager"),
        ("Order Manager", "Order Manager"),
    )

    uid = models.UUIDField(
        unique=True, 
        default=uuid.uuid4,
        editable=False, 
        db_index=True
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_image = models.ImageField(
        upload_to="employees/", 
        null=True, 
        blank=True
    )
    phone = models.CharField(max_length=15)
    address = models.TextField()
    role = models.CharField(max_length=20, choices=ROLE, default="Admin")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.get_full_name() or self.user.username
    
