from rest_framework import serializers
from .models import CustomUser
from django.contrib.auth.password_validation import validate_password

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

class RegisterSerializer(serializers.ModelSerializer):
    """
    Serializer for user registration.
    Validates password and creates a new user with hashed password.
    """
    password = serializers.CharField(
        write_only=True,
        required=True,
        validators=[validate_password],
    )

    class Meta:
        model = CustomUser
        fields = ["username", "password", "email", "first_name", "last_name"]

    def create(self, validated_data):
        return CustomUser.objects.create_user(
            username=validated_data["username"],
            email=validated_data["email"],
            password=validated_data["password"],
            first_name=validated_data.get("first_name", ""),
            last_name=validated_data.get("last_name", ""),
        )