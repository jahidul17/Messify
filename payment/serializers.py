from rest_framework import serializers
from .models import Payment

class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model=Payment
        fields='__all__'
        read_only_fields=('transaction_id','status','payment_date','created_at')
        


