from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import Payment
from .serializers import PaymentSerializer
from .utils import initiate_sslcommerz_payment
from rest_framework.views import APIView
from django.utils import timezone

# class PaymentInitiateView(generics.GenericAPIView):
#     serializer_clas=PaymentSerializer
#     permission_classes=[IsAuthenticated]
    
#     def post(self,request):
#         bill_id=request.data.get('bill_id')
#         payment_method=request.data.get('payment_method')
        
#         from billing.models import Bill
#         try:
#             bill=Bill.objects.get(id=bill_id,member=request.user.memberprofile)
#         except Bill.DoesNotExist:
#             return Response({"error":"Bill not found"},status=404)
        
#         payment=Payment.objects.create(
#             member=request.user.memberprofile,
#             bill=bill,
#             payment_method=payment_method,
#             paid_amount=bill.total_amount
#         )
        
#         payment_url=initiate_sslcommerz_payment(payment)
#         return Response({
#             "transaction_id":payment.transaction_id,
#             "payment_url":payment_url,
#         })
        
class PaymentHistoryView(generics.ListAPIView):
    serializer_class=PaymentSerializer
    permission_classes=[IsAuthenticated]
    
    def get_queryset(self):
        return Payment.objects.filter(member=self.request.user.memberprofile).order_by('-payment_date')
     


class PaymentCallbackView(APIView):
    authentication_classes = []  
    permission_classes = []

    def post(self, request):
        tran_id = request.data.get('tran_id')
        status = request.data.get('status')
        amount = request.data.get('amount')

        if not tran_id:
            return Response({"error": "Transaction ID missing"}, status=400)

        try:
            payment = Payment.objects.get(transaction_id=tran_id)
        except Payment.DoesNotExist:
            return Response({"error": "Invalid transaction"}, status=400)

        
        if str(payment.paid_amount) != str(amount):
            payment.status = 'FAILED'
            payment.save()
            return Response({"error": "Amount mismatch"}, status=400)

        
        if status in ['VALID', 'SUCCESS']:
            payment.status = 'SUCCESS'
            payment.payment_date = timezone.now()
            payment.save()
            payment.bill.is_paid = True
            payment.bill.save()
        else:
            payment.status = 'FAILED'
            payment.save()

        return Response({"message": "Payment updated successfully"})


