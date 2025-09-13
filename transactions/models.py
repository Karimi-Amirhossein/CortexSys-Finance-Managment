from django.db import models
from django.conf import settings


class Transaction(models.Model):
    """
    Represents a single financial transaction (either income or expense)
    linked to a specific user.
    """

    class TransactionType(models.TextChoices):
        INCOME = "INCOME", "Income"
        EXPENSE = "EXPENSE", "Expense"

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="transactions",
    )

    title = models.CharField(max_length=200)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    type = models.CharField(
        max_length=7,
        choices=TransactionType.choices,
        default=TransactionType.EXPENSE,
    )
    category = models.CharField(max_length=100, blank=True)
    date = models.DateField()
    notes = models.TextField(blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-date", "-created_at"]
        verbose_name = "Transaction"
        verbose_name_plural = "Transactions"

    def __str__(self):
        return f"{self.title} | {self.get_type_display()} | {self.amount} on {self.date}"
