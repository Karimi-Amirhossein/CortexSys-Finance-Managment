from rest_framework import serializers
from .models import Transaction
from accounts.serializers import UserSerializer


class TransactionSerializer(serializers.ModelSerializer):
    """
    Serializer for the Transaction model.
    Converts Transaction instances to/from JSON.
    """

    user = UserSerializer(read_only=True)  # Set automatically from request in views

    class Meta:
        model = Transaction
        fields = [
            "id",
            "user",
            "title",
            "amount",
            "type",
            "category",
            "date",
            "notes",
            "created_at",
            "updated_at",
        ]
        read_only_fields = ["created_at", "updated_at"]

    def validate_amount(self, value):
        """Ensure the transaction amount is positive."""
        if value <= 0:
            raise serializers.ValidationError("Amount must be greater than zero.")
        return value
