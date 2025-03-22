import uuid
from django.db import models

from customers.models import Customer
from medicines.models import Medicine
from users.models import Employee

class Order(models.Model):
    uid = models.UUIDField(
        unique=True, 
        default=uuid.uuid4,
        editable=False, 
        db_index=True
    )
    order_no = models.CharField(max_length=20, unique=True)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    medicine = models.ForeignKey(Medicine, on_delete=models.CASCADE)
    total_pack = models.PositiveBigIntegerField()
    order_amount = models.DecimalField(max_digits=9, decimal_places=2)
    order_date = models.DateTimeField(auto_now_add=True)
    ordered_by = models.ForeignKey(Employee, on_delete=models.SET_NULL, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        if not self.order_no:
            unique_id = str(uuid.uuid4().int)[0:6]
            self.order_no = f"ORD{unique_id}"
        
        customer, created = Customer.objects.get_or_create(
            phone = self.customer.phone, 
            name = self.customer.name,
            defaults={
                "name": self.customer.name,
                "phone": self.customer.phone,
            }
        )
        self.customer = customer

        super().save(*args, **kwargs)

    def __str__(self):
        return f"Order {self.order_no} - {self.customer.name}"
    