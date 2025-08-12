from django.contrib.auth.forms import AuthenticationForm, UserChangeForm
from django import forms
from .models import User

class LoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update(
            {'class': 'form-control', 'placeholder': 'Username'}
        )
        self.fields['password'].widget.attrs.update(
            {'class': 'form-control', 'placeholder': '*********'}
        )

class CustomUserChangeForm(UserChangeForm):
    password = None  # Remove password field

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name in self.fields:
            self.fields[field_name].widget.attrs.update({'class': 'form-control'})
