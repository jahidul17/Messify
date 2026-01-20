from django.urls import path
from .views import MemberBillListView,GenerateMonthlyBillView

urlpatterns=[
    path('',MemberBillListView.as_view()),
    path('generate/',GenerateMonthlyBillView.as_view()),
]

