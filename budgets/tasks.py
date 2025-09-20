from decimal import Decimal
from celery import shared_task
from django.utils import timezone
from django.db.models import Sum
from .models import Budget
from transactions.models import Transaction
import logging

logger = logging.getLogger(__name__)

@shared_task
def check_budgets():
    """
    Celery task to check active budgets and warn if spending
    has passed a defined threshold (e.g. 80%).
    """
    logger.info("Starting budget check task...")

    today = timezone.now().date()
    threshold = Decimal("0.80")  # 80%

    # Find all budgets that are active today
    active_budgets = Budget.objects.filter(
        start_date__lte=today,
        end_date__gte=today
    )

    for budget in active_budgets:
        # Sum all expenses for this budget's category and period
        total_expenses = Transaction.objects.filter(
            user=budget.user,
            type="EXPENSE",
            date__range=[budget.start_date, budget.end_date],
            category=budget.category  # assumes same category model
        ).aggregate(total=Sum("amount"))["total"] or Decimal("0.00")

        # If spending exceeds the threshold, log a warning
        if total_expenses >= budget.total_amount * threshold:
            logger.warning(
                f"[Budget Alert] User {budget.user.username} has spent "
                f"{threshold * 100}% or more of their '{budget.category}' budget "
                f"({budget.title})."
            )
            # TODO: send email/notification in future

    logger.info(f"Budget check finished. {active_budgets.count()} budgets checked.")
    return f"Checked {active_budgets.count()} active budgets."
