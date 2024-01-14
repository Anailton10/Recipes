from django import forms
from django.contrib.auth.models import User


def add_attr(field, attr_name, attr_new_vall):
    existing_attr = field.widget.attrs.get(attr_name, '')
    field.widget.attrs[attr_name] = f'{existing_attr} {attr_new_vall}'.strip


def add_placeholder(field, placeholder_val):
    field.widget.attrs['placeholder'] = placeholder_val


class RegisterForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        add_placeholder(
            field=self.fields['username'], placeholder_val='Your username')
        add_placeholder(
            field=self.fields['email'], placeholder_val='Your e-mail')
        add_placeholder(
            field=self.fields['first_name'], placeholder_val='Your first name'
        )
        add_placeholder(
            field=self.fields['last_name'], placeholder_val='Your last name'
        )
        add_placeholder(
            field=self.fields['password'], placeholder_val='Your password'
        )

    password = forms.CharField(
        required=True,
        widget=forms.PasswordInput(attrs={'placeholder': 'Your password'}),
        error_messages={
            'required': 'Password must be valid'
        },
        help_text=(
            'Password must have at least one uppercase letter, '
            'one lowercase letter and one number. The length should be '
            'at least 8 characters.'
        )
    )
    password2 = forms.CharField(
        required=True,
        widget=forms.PasswordInput(attrs={
            'placeholder': 'Repeat your password'
        }),
        error_messages={
            'required': 'Password must be valid'
        }
    )

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
            },

            'password': {
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
