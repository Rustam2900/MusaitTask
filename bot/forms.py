from django import forms
from django.contrib.auth.forms import UserCreationForm
from bot.models import User, Reminder


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


class ReminderForm(forms.ModelForm):
    class Meta:
        model = Reminder
        fields = ['title', 'content', 'date', 'status']
        widgets = {
            'date': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        }