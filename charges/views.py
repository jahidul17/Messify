from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from django.utils.timezone import now

from .models import MonthlyCharge
from .serializers import MonthlyChargeSerializer
from .permissions import IsAdmin

class MonthlyChargeCreateView(generics.CreateAPIView):
    queryset = MonthlyCharge.objects.all()
    serializer_class = MonthlyChargeSerializer
    permission_classes = [IsAdmin]


class MonthlyChargeUpdateView(generics.UpdateAPIView):
    queryset = MonthlyCharge.objects.all()
    serializer_class = MonthlyChargeSerializer
    permission_classes = [IsAdmin]


class CurrentMonthlyChargeView(generics.RetrieveAPIView):
    serializer_class = MonthlyChargeSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        today = now().date()
        return MonthlyCharge.objects.filter(
            effective_month__lte=today
        ).order_by('-effective_month').first()
        



class MonthlyChargeListView(generics.ListAPIView):
    queryset = MonthlyCharge.objects.all()
    serializer_class = MonthlyChargeSerializer
    permission_classes = [IsAuthenticated]


