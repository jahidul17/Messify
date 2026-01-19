from django.db import models
from members.models import MemberProfile as Member
from django.utils import timezone

class Bill(models.Model):
    PAYMENTS_STATUS=(
        ('PENDING','Pending'),
        ('PAID', 'Paid'),
    )
    
    member=models.ForeignKey(Member, on_delete=models.CASCADE, related_name='bills')
    month=models.DateField()
    
    seat_rent_amount=models.DecimalField(max_digits=10, decimal_places=2)
    meal_bill_amount=models.DecimalField(max_digits=10, decimal_places=2)
    electricity_amount=models.DecimalField(max_digits=10,decimal_places=2)
    water_amount=models.DecimalField(max_digits=10, decimal_places=2)
    utility_amount=models.DecimalField(max_digits=10, decimal_places=2)
    
    total_amount=models.DecimalField(max_digits=10,decimal_places=2)
    payment_status=models.CharField(max_length=10, choices=PAYMENTS_STATUS, default='PENDING')

    created_at=models.DateField(auto_now_add=True)
    
    class Meta:
        unique_together=('member','month')
        
    def __str__(self):
        return f"{self.member.full_name}-{self.month}"





