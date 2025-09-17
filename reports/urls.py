from django.urls import path
from .views import FinancialSummaryReportView

#Namespace for the report app
app_name = "reports"

urlpatterns = [
    # Financial summary report endpoint
    # Example: GET /api/reports/summary/?year=2025&month=9
    path ("summary/", FinancialSummaryReportView.as_view(), name="financial-summary"),
]
