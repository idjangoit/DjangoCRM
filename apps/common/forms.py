from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class SignUpForm(forms.ModelForm):
    """Form definition for User."""
    first_name = forms.CharField(
        max_length=30, required=False, help_text='Optional')
    last_name = forms.CharField(
        max_length=30, required=False, help_text='Optional')
    email = forms.EmailField(
        max_length=254, help_text='Enter a valid email address')

    class Meta:
        """Meta definition for Userform."""

        model = User
        fields = ('username', 'first_name', 'last_name',
                  'email', 'password1', 'password2',)
