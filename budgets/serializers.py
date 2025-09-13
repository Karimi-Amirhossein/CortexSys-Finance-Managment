from rest_framework import serializers
from .models import Budget
from accounts.serializers import UserSerializer

class BudgetSerializer(serializers.ModelSerializer):
    """
    Serializer for the Budget model.
    Includes nested user details and validation.
    """
    
    user = UserSerializer(read_only=True)  # Set automatically from request in views
    display_name = serializers.SerializerMethodField()

    class Meta:
        model = Budget
        fields = [
            "id",
            "user",
            "title",
            "total_amount",
            "start_date",
            "end_date",
            "category",
            "created_at",
            "updated_at",
            "display_name",
        ]
        read_only_fields = ["created_at", "updated_at"]

    def get_display_name(self, obj):
        """Returns a readable string for the budget."""
        return f"{obj.title} ({obj.total_amount}) | {obj.start_date} → {obj.end_date}"

    def validate(self, data):
        """Ensure start_date is before end_date."""
        if data['start_date'] > data['end_date']:
            raise serializers.ValidationError("End date must occur after start date.")
        return data

    def validate_total_amount(self, value):
        """Ensure total_amount is positive."""
        if value <= 0:
            raise serializers.ValidationError("Total amount must be greater than zero.")
        return value
