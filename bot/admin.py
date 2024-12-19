from django.contrib import admin
from modeltranslation.admin import TranslationAdmin

from bot.models import User, Reminder, Admin


@admin.register(User)
class UserAdmin(TranslationAdmin):
    list_display = ('id', 'username', 'phone_number')
    list_display_links = ('id', 'username', 'phone_number')
    search_fields = ('username', 'phone_number')


@admin.register(Reminder)
class ReminderAdmin(TranslationAdmin):
    list_display = ('title', 'user', 'date', 'status')
    search_fields = ('title', 'user__email')
    list_filter = ('status', 'date')


@admin.register(Admin)
class ReminderAdmin(admin.ModelAdmin):
    list_display = ('id', 'telegram_id', 'create_at')
    search_fields = ('telegram_id',)
    list_filter = ('telegram_id',)
