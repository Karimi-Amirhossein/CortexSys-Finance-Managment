import logging
from rest_framework import generics, permissions, filters
from django_filters.rest_framework import DjangoFilterBackend
from .models import Transaction
from .serializers import TransactionSerializer
from .pagination import StandardResultsSetPagination

logger = logging.getLogger(__name__)

class TransactionListCreateView(generics.ListCreateAPIView):
    """
    API endpoint for listing and creating user transactions.
    Supports filtering, ordering, and pagination.
    """

    serializer_class = TransactionSerializer
    permission_classes = [permissions.IsAuthenticated]
    pagination_class = StandardResultsSetPagination

    # Add filtering and ordering capabilities
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter]
    filterset_fields = ['type', 'category', 'date']
    ordering_fields = ['date', 'amount', 'created_at']
    search_fields = ['title', 'category', 'notes']


    def get_queryset(self):
        """ Returns transactions belonging only to the logged-in user. """
        return (
            Transaction.objects
            .filter(user=self.request.user)
            .select_related("user")
        )

    def perform_create(self, serializer):
        """ Set the user to the logged-in user automatically. """
        transaction = serializer.save(user=self.request.user)
        logger.info(f"Transaction created for user {self.request.user.id}: {transaction.id}")