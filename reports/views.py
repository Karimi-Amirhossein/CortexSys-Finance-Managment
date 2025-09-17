from decimal import Decimal
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions, status
from django.db.models import Sum
from django.utils import timezone
from transactions.models import Transaction

class FinancialSummaryReportView(APIView):
    """
    API endpoint to provide a financial summary for a given month and year.
    Defaults to the current month and year if not provided. 
    """

    permission_class = [permissions.IsAuthenticated]

    def get(self, request, *args, **kwargs):
        # Get year/month from query params or fallback to current
        year = request.query_params.get('year', timezone.now().year)
        month = request.query_params.get('month', timezone.now().month)

        try:
            year, month = int(year), int(month)
        except (ValueError, TypeError):
            return Response(
                {"Error": "Year and month must be valid integers."},
                status=status.HTTP_400_BAD_REQUEST
            )
        
        #Filter transactions for this user and period
        queryset = Transaction.objects.filter(
            user = request.user,
            date__year = year,
            date__month = month
        )

        #Calculate totals
        total_income = queryset.filter(type="INCOME").aggregate(
            total = Sum('amount')
        )['total'] or Decimal('0.00')

        total_expense = queryset.filter(type="EXPENSE").aggregate(
            total = Sum('amount')
        )['total'] or Decimal('0.00')

        net_savings = total_income - total_expense

        #Response payLoad
        return Response({
            "report_period": f"{year}-{month:02d}",
            "total_income": total_income,
            "total_expense": total_expense,
            "net_savings": net_savings,
            "message": "Financial summary generated successfully."
        }, status=status.HTTP_200_OK)
    