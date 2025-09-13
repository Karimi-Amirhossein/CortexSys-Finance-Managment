from django.db import models
from django.conf import settings


class Budget(models.Model):
    """
    Represents a budget set by a user for a specific period or category.
    """

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="budgets",
    )

    title = models.CharField(max_length=200)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)

    start_date = models.DateField()
    end_date = models.DateField()
    category = models.CharField(max_length=100, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-end_date", "-created_at"]
        verbose_name = "Budget"
        verbose_name_plural = "Budgets"

    def __str__(self):
        return f"{self.title} | {self.total_amount} | {self.start_date} → {self.end_date}"
