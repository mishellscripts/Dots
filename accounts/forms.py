from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class UserCreateForm(UserCreationForm):
    class Meta:
        fields = ("username", "email", "password1", "password2")
        model = User

    # Look into why this would result in error
    """def __init__(self, *args, **kwargs):
        super().__init__(self, *args, **kwargs)
        self.fields["email"].label = "Email Address"
    """