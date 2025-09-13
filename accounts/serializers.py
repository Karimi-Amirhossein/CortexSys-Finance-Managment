from rest_framework import serializers
from .models import CustomUser

class UserSerializer(serializers.ModelSerializer):
    """
    Serializer for the CustomUser model.
    Displays user information without exposing sensitive data like password.
    """
    
    full_name = serializers.SerializerMethodField()

    class Meta:
        model = CustomUser
        fields = ['id', 'username', 'email', 'first_name', 'last_name', 'full_name']
        extra_kwargs = {field: {'read_only': True} for field in fields}

    def get_full_name(self, obj):
        """Returns the user's full name."""
        return f"{obj.first_name} {obj.last_name}".strip()
