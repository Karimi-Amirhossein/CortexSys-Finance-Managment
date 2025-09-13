from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _


class CustomUser(AbstractUser):
    """
    Custom User model extending Django's AbstractUser.

    Email is used as the unique identifier for authentication instead of username.
    """
    
    # We don't need the default username field from AbstractUser anymore,
    # but we keep it for Django's internal processes. We can make it non-editable.
    # The `email` field is now the primary field for login.
    
    email = models.EmailField(
        _('email address'),
        unique=True,  # This makes sure no two users can have the same email.
        help_text='Required. Please enter your email address.'
    )

    is_verified = models.BooleanField(
        default=False,
        help_text='Indicates if the user has verified their email address.'
    )

    # Set the email field as the main username field.
    USERNAME_FIELD = 'email'
    
    # The default username field is still required by some Django internals.
    # We list it here, but we will ask for it upon registration.
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        """
        Returns the string representation of the User object, which is the email.
        """
        return self.email
    