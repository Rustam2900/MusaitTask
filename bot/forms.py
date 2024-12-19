from django import forms
from django.contrib.auth.forms import UserCreationForm
from bot.models import User, Reminder
from django.core.exceptions import ValidationError


class RegistrationForm(UserCreationForm):
    username = forms.CharField(
        max_length=255,
        required=True,
        label="username",
        widget=forms.TextInput(attrs={'placeholder': 'username kiriting'})
    )
    email = forms.EmailField(
        required=True,
        label="Email",
        widget=forms.EmailInput(attrs={'placeholder': 'email kiriting'})
    )
    phone_number = forms.CharField(
        max_length=20,
        required=True,
        label="Phone Number",
        widget=forms.TextInput(attrs={'placeholder': 'number: +998930682911'})
    )

    class Meta:
        model = User
        fields = ['email', 'username', 'phone_number', 'password1', 'password2']
        widgets = {
            'password1': forms.PasswordInput(attrs={'placeholder': 'Enter your password'}),
            'password2': forms.PasswordInput(attrs={'placeholder': 'Confirm your password'}),
        }

    def clean_email(self):
        email = self.cleaned_data['email']
        if User.objects.filter(email=email).exists():
            raise ValidationError(f"Email {email} allaqachon mavjud.")
        return email

    def clean_phone_number(self):
        phone_number = self.cleaned_data['phone_number']
        if User.objects.filter(
                phone_number=phone_number).exists():
            raise ValidationError(f"Phone number {phone_number} allaqachon mavjud.")
        return phone_number


class ReminderForm(forms.ModelForm):
    class Meta:
        model = Reminder
        fields = ['title', 'content', 'date', 'status']
        widgets = {
            'date': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        }
