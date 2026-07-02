from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User


class VendorRegistrationForm(UserCreationForm):

    email = forms.EmailField()
    company_name = forms.CharField(
        max_length=255
    )

    phone = forms.CharField(
        max_length=20
    )

    address = forms.CharField(
        widget=forms.Textarea,
        required=False
    )
    class Meta:
        model = User

        fields = (
            'username',
            'email',
            'password1',
            'password2',
            'company_name',
            'phone',
            'address'
        )