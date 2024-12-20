from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractUser, UserManager
from django.contrib.auth.hashers import make_password
from bot.validators import phone_number_validator
from django.conf import settings


class CustomUserManager(UserManager):
    def _create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError("The email must be set")
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.password = make_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", False)
        extra_fields.setdefault("is_superuser", False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True.")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")

        return self._create_user(email, password, **extra_fields)


class User(AbstractUser):
    email = models.EmailField(unique=True)
    full_name = models.CharField(_("full name"), blank=True, max_length=255)
    username = models.CharField(_("username"), blank=True, max_length=255, null=True)
    phone_number = models.CharField(_("phone number"), blank=True, unique=True, validators=[phone_number_validator],
                                    max_length=20)
    telegram_id = models.CharField(_("telegram id"), blank=True, null=True, max_length=255, unique=True)
    tg_username = models.CharField(
        _("telegram username"), blank=True, null=True, max_length=255, unique=True)
    password = models.CharField(_("password"), blank=True, max_length=255)
    create_at = models.DateTimeField(auto_now_add=True)

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    groups = None
    user_permissions = None

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'

    def __str__(self):
        return f"Email: {self.email}"


class Reminder(models.Model):
    STATUS_CHOICES = [
        ('pending', _('Pending')),
        ('completed', _('Completed')),
    ]

    title = models.CharField(_("title"), max_length=255)
    content = models.TextField(_("content"))
    date = models.DateTimeField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')

    class Meta:
        verbose_name = _("Reminder")
        verbose_name_plural = _("Reminders")
        ordering = ['-date']

    def __str__(self):
        return self.title


class Admin(models.Model):
    telegram_id = models.BigIntegerField(unique=True)
    create_at = models.DateTimeField(auto_now_add=True)
