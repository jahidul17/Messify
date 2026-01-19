from django.urls import path
from .views import (
    MonthlyChargeCreateView,
    MonthlyChargeUpdateView,
    CurrentMonthlyChargeView,
    MonthlyChargeListView
)

urlpatterns = [
    path('create/', MonthlyChargeCreateView.as_view()),
    path('update/<int:pk>/', MonthlyChargeUpdateView.as_view()),
    path('current/', CurrentMonthlyChargeView.as_view()),
    path('list/', MonthlyChargeListView.as_view()),
]
