import uuid
from django.db import models


class Category(models.Model):
    uid = models.UUIDField(
        unique=True, 
        default=uuid.uuid4,
        editable=False, 
        db_index=True
    )
    category_name = models.CharField(max_length=255, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.category_name


class Medicine(models.Model):
    STATUS = (
        ("Available", "Available"),
        ("Out of Stock", "Out of Stock"),
    )

    uid = models.UUIDField(
        unique=True, 
        default=uuid.uuid4,
        editable=False, 
        db_index=True
    )
    name = models.CharField(max_length=255)
    brand_name = models.CharField(max_length=255)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    unit_price = models.DecimalField(max_digits=9, decimal_places=2)
    pack_size = models.CharField(max_length=100)
    total_pack = models.PositiveBigIntegerField()
    status = models.CharField(max_length=20, choices=STATUS, default="Available")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name} - {self.brand_name}"
    

class MedicineStock(models.Model):
    uid = models.UUIDField(
        unique=True, 
        default=uuid.uuid4,
        editable=False, 
        db_index=True
    )
    medicine_name = models.ForeignKey(Medicine, on_delete=models.CASCADE)
    total_pack = models.PositiveBigIntegerField()
    purchase_price = models.DecimalField(max_digits=9, decimal_places=2)
    date = models.DateField(auto_now_add=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.medicine_name} - {self.total_pack} packs"
