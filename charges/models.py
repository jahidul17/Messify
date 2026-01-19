from django.db import models

class MonthlyCharge(models.Model):
    effective_month = models.DateField(
        help_text="Use first day of month, e.g. 2026-01-01"
    )

    meal_rate = models.DecimalField(
        max_digits=6, decimal_places=2,
        help_text="Rate per meal"
    )
    electricity_bill = models.DecimalField(
        max_digits=8, decimal_places=2
    )
    water_bill = models.DecimalField(
        max_digits=8, decimal_places=2
    )
    utility_charge = models.DecimalField(
        max_digits=8, decimal_places=2
    )

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-effective_month']
        unique_together = ['effective_month']

    def __str__(self):
        return f"Charges for {self.effective_month.strftime('%B %Y')}"

