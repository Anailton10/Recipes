from django import forms
from django.contrib.auth.models import User


class RegisterForm(forms.ModelForm):
    class Meta:
        model = User
        fields = [
            'first_name',
            'last_name',
            'username',
            'email',
            'password',
        ]
        # exclude = ['first_name']
        labels = {
            'first_name': 'First name',
            'last_name': 'Last name',
            'username': 'Username',
            'email': 'Email',
            'password': 'Password',
        }

        help_texts = {
            'email': 'The e-mail must be valid',
        }

        error_messages = {
            'username': {
                'required': 'This field must not be empty',
            }
        }

        widgets = {
            'first_name': forms.TextInput(attrs={
                'placeholder': 'Type your first name here...'
            }),

            'last_name': forms.TextInput(attrs={
                'placeholder': 'Type your last name here...'
            }),

            'username': forms.TextInput(attrs={
                'placeholder': 'Type your username here...'
            }),

            'email': forms.EmailInput(attrs={
                'placeholder': 'Type your e-mail here...'
            }),

            'password': forms.PasswordInput(attrs={
                'placeholder': 'Type your password here...'
            })
        }
