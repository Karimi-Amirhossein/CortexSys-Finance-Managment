import logging
from rest_framework import generics, permissions, filters
from django_filters.rest_framework import DjangoFilterBackend
from .models import Transaction
from .serializers import TransactionSerializer
from .pagination import StandardResultsSetPagination
from .permissions import IsOwner

logger = logging.getLogger(__name__)

class TransactionListCreateView(generics.ListCreateAPIView):
    """
    API endpoint for listing and creating user transactions.
    Supports filtering, ordering, and pagination.
    """
    serializer_class = TransactionSerializer
    permission_classes = [permissions.IsAuthenticated]
    pagination_class = StandardResultsSetPagination
    
    # Configuration for filtering, searching, and ordering
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['type', 'category', 'date']
    search_fields = ['title', 'category', 'notes']
    ordering_fields = ['date', 'amount', 'created_at']

    def get_queryset(self):
        """Returns transactions belonging only to the logged-in user."""
        return Transaction.objects.filter(user=self.request.user).select_related("user")

    def perform_create(self, serializer):
        """Automatically assigns the logged-in user as the owner of the transaction."""
        transaction = serializer.save(user=self.request.user)
        logger.info(f"Transaction created for user {self.request.user.id}: {transaction.id}")

class TransactionDetailView(generics.RetrieveUpdateDestroyAPIView):
    """
    API endpoint for retrieving, updating, or deleting a single transaction.
    Access is restricted to the owner of the transaction.
    """
    serializer_class = TransactionSerializer
    permission_classes = [permissions.IsAuthenticated, IsOwner]

    def get_queryset(self):
        """Ensures that the user can only access their own transactions."""
        return Transaction.objects.filter(user=self.request.user)