from django.urls import path
from .views import PaymentInitiateView,PaymentHistoryView,PaymentCallbackView

urlpatterns = [
    path('initiate/',PaymentInitiateView.as_view(),name='payment-initiate'),
    path('history/',PaymentHistoryView.as_view(),name='payment-history'),
    path('callback/', PaymentCallbackView.as_view(), name='payment-callback'),
]


