from django.contrib.auth.forms import BaseUserCreationForm

from apps.models import User


class CustomBaseUserCreationForm(BaseUserCreationForm):
    class Meta(BaseUserCreationForm.Meta):
        model = User


class CustomUserCreationForm(BaseUserCreationForm):
    pass
