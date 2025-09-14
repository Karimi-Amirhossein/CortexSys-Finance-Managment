import logging
from rest_framework import generics, permissions, filters
from django_filters.rest_framework import DjangoFilterBackend
from .models import Budget
from .serializers import BudgetSerializer
from transactions.pagination import StandardResultsSetPagination

logger = logging.getLogger(__name__)

class BudgetListCreateView(generics.ListCreateAPIView):
    """
    API endpoint for listing and creating user budgets.
    - Authenticated users only
    - Each user can only access their own budgets
    - Supports filtering and ordering
    - Uses custom pagination for structured responses
    """

    serializer_class = BudgetSerializer
    permission_classes = [permissions.IsAuthenticated]
    pagination_class = StandardResultsSetPagination

    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    filterset_fields = ['category', 'start_date', 'end_date']
    ordering_fields = ['start_date', 'end_date', 'total_amount']

    def get_queryset(self):
        return (
            Budget.objects
            .filter(user=self.request.user)
            .select_related("user")
        )

    def perform_create(self, serializer):
        budget = serializer.save(user=self.request.user)
        logger.info(f"Budget created for user {self.request.user.id}: {budget.id}")
