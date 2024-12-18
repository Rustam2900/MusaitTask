from modeltranslation.translator import TranslationOptions, register
from bot import models


@register(models.User)
class UserTranslation(TranslationOptions):
    fields = ('full_name', 'username')


@register(models.Reminder)
class ReminderTranslation(TranslationOptions):
    fields = ('title', 'content')
