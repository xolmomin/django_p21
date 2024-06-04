from django.contrib.auth.forms import BaseUserCreationForm, UserCreationForm
from django.core.exceptions import ValidationError
from django.forms import EmailField

from apps.models import User


class CustomBaseUserCreationForm(BaseUserCreationForm):
    email = EmailField()

    class Meta(BaseUserCreationForm.Meta):
        model = User
        fields = ("username", 'email')


class CustomUserCreationForm(CustomBaseUserCreationForm):
    def clean_username(self):
        """Reject usernames that differ only in case."""
        username = self.cleaned_data.get("username")
        if (
                username
                and self._meta.model.objects.filter(username__iexact=username).exists()
        ):
            self._update_errors(
                ValidationError(
                    {
                        "username": self.instance.unique_error_message(
                            self._meta.model, ["username"]
                        )
                    }
                )
            )
        else:
            return username

