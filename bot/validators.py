import re
from django.core.exceptions import ValidationError


def phone_number_validator(value):
    regex = re.compile(r'^\+998\s\d{2}\s\d{3}\s\d{2}\s\d{2}$')

    if not regex.match(value):
        raise ValidationError("Telefon raqami noto'g'ri formatda. To'g'ri format: +998 XX XXX XX XX")


def validate_email(email):
    pattern = r'^[\w\.-]+@[a-zA-Z\d\.-]+\.[a-zA-Z]{2,}$'
    return re.match(pattern, email)


def validate_password(password):
    if len(password) < 8:
        return False
    return True
