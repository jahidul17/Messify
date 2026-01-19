from rest_framework import serializers
from .models import MonthlyCharge

class MonthlyChargeSerializer(serializers.ModelSerializer):
    class Meta:
        model = MonthlyCharge
        fields = '__all__'
