from django.urls import path
from .views import MealCreateView, MealListView,MonthlyMealCountView

urlpatterns = [
    path('create/', MealCreateView.as_view()),
    path('my-meals/', MealListView.as_view()),
    path('count/', MonthlyMealCountView.as_view()),
 
]

