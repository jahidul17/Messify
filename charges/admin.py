from django.contrib import admin
from django.core.exceptions import ValidationError
from .models import MonthlyCharge


@admin.register(MonthlyCharge)
class MonthlyChargeAdmin(admin.ModelAdmin):
    list_display = (
        'effective_month',
        'meal_rate',
        'electricity_bill',
        'water_bill',
        'utility_charge',
        'created_at',
    )

    list_filter = (
        'effective_month',
    )

    ordering = ('-effective_month',)

    readonly_fields = (
        'created_at',
    )

    fieldsets = (
        ("Month Configuration", {
            'fields': ('effective_month',)
        }),
        ("Meal Rate", {
            'fields': ('meal_rate',)
        }),
        ("Monthly Fixed Charges", {
            'fields': (
                'electricity_bill',
                'water_bill',
                'utility_charge',
            )
        }),
        ("System Info", {
            'fields': ('created_at',)
        }),
    )

    search_fields = (
        'effective_month',
    )

    def save_model(self, request, obj, form, change):
        if obj.effective_month.day != 1:
            raise ValidationError(
                "Effective month must be the first day of the month (e.g. 2026-01-01)."
            )
        super().save_model(request, obj, form, change)

