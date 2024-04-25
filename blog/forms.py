# blog/forms.py

from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class CommentForm(forms.Form):
    body = forms.CharField(
        widget=forms.Textarea(
            attrs={
                "class": "font-karma bg-gray-100 rounded border border-gray-400 leading-normal w-full py-2 px-3  placeholder-gray-700 focus:outline-none focus:bg-white",
                "placeholder": "Leave a comment...",
            }
        )
    )


class SignupForm(UserCreationForm):
    first_name = forms.CharField(
        max_length=100,
        widget=forms.TextInput(
            attrs={
                "class": "font-karma text-black appearance-none block w-full bg-gray-200 border border-gray-200 rounded py-3 px-4 mb-3 leading-tight focus:outline-none focus:bg-white",
                "id": "grid-first-name",
                "type": "text",
            }
        ),
    )
    last_name = forms.CharField(
        max_length=100,
        widget=forms.TextInput(
            attrs={
                "class": "font-karma text-black appearance-none block w-full bg-gray-200 border border-gray-200 rounded py-3 px-4 mb-3 leading-tight focus:outline-none focus:bg-white",
                "id": "grid-last-name",
                "type": "text",
            }
        ),
    )
    username = forms.CharField(
        max_length=50,
        widget=forms.TextInput(
            attrs={
                "class": "font-karma text-black appearance-none block w-full bg-gray-200  border border-gray-200 rounded py-3 px-4 mb-3 leading-tight focus:outline-none focus:bg-white",
                "id": "grid-username",
                "type": "text",
            }
        ),
    )
    email = forms.EmailField(
        widget=forms.EmailInput(
            attrs={
                "class": "font-karma text-black appearance-none block w-full bg-gray-200  border border-gray-200 rounded py-3 px-4 mb-3 leading-tight focus:outline-none focus:bg-white",
                "id": "grid-first-name",
                "type": "email",
            }
        )
    )
    password = forms.CharField(
        max_length=128,
        widget=forms.PasswordInput(
            attrs={
                "class": "font-karma text-black appearance-none block w-full bg-gray-200 border border-gray-200 rounded py-3 px-4 mb-3 leading-tight focus:outline-none focus:bg-white",
                "id": "grid-password",
                "type": "password",
                "placeholder": "***********",
            }
        ),
    )
    confirm_password = forms.CharField(
        max_length=128,
        widget=forms.PasswordInput(
            attrs={
                "class": "font-karma text-black appearance-none block w-full bg-gray-200 border border-gray-200 rounded py-3 px-4 mb-3 leading-tight focus:outline-none focus:bg-white",
                "id": "grid-confirm-password",
                "type": "password",
                "placeholder": "***********",
            }
        ),
    )
    profile_upload = forms.ImageField(
        required=False,
        widget=forms.FileInput(
            attrs={
                "id": "grid-confirm-password",
                "type": "file",
            }
        ),
    )

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")

        if password != confirm_password:
            raise forms.ValidationError("The passwords do not match.")


class LoginForm(forms.Form):
    email = forms.EmailField(
        widget=forms.EmailInput(
            attrs={
                "class": "font-karma text-black appearance-none block w-full bg-gray-200  border border-gray-200 rounded py-3 px-4 mb-3 leading-tight focus:outline-none focus:bg-white",
                "id": "grid-first-name",
                "type": "email",
            }
        )
    )
    password = forms.CharField(
        max_length=128,
        widget=forms.PasswordInput(
            attrs={
                "class": "font-karma text-black appearance-none block w-full bg-gray-200 border border-gray-200 rounded py-3 px-4 mb-3 leading-tight focus:outline-none focus:bg-white",
                "id": "grid-password",
                "type": "password",
                "placeholder": "***********",
            }
        ),
    )
