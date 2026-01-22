from django.db import models
from django.db import models
from members.models import MemberProfile
from billing.models import Bill


class Payment(models.Model):
    STATUS_CHOICES = (
        ('PENDING', 'Pending'),
        ('SUCCESS', 'Success'),
        ('FAILED', 'Failed'),
        ('CANCELLED', 'Cancelled'),
    )

    member = models.ForeignKey(
        MemberProfile,
        on_delete=models.CASCADE,
        related_name='payments'
    )
    bill = models.ForeignKey(
        Bill,
        on_delete=models.CASCADE,
        related_name='payments'
    )

    payment_method = models.CharField(
        max_length=30,
        choices=(
            ('SSLCOMMERZ', 'SSLCommerz'),
            ('HANDCASH', 'HandCash'),
        )
    )

    transaction_id = models.CharField(
        max_length=100,
        unique=True,
        blank=True,
        null=True
    )

    paid_amount = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )

    payment_date = models.DateTimeField(
        blank=True,
        null=True
    )

    status = models.CharField(
        max_length=15,
        choices=STATUS_CHOICES,
        default='PENDING'
    )

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.member} - {self.transaction_id}"

