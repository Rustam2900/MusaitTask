from celery import shared_task
from aiogram import Bot
from django.conf import settings

from django.core.mail import send_mail

from bot.models import Reminder

bot = Bot(token=settings.BOT_TOKEN)


@shared_task
def send_reminder(reminder_id):
    try:
        reminder = Reminder.objects.get(id=reminder_id)
        print("####################################################################", reminder.title)
        message = f"Eslatma: {reminder.title}\n\n{reminder.content}"
        send_mail(
            subject="Siz uchun eslatma!",
            message=message,
            from_email="jumanazarustam@gmail.com",
            recipient_list=[reminder.user.email]
        )

        reminder.status = 'completed'
        reminder.save()
    except Reminder.DoesNotExist:
        return f"not"


@shared_task
def send_reminder(reminder_id):
    try:
        reminder = Reminder.objects.get(id=reminder_id)
        print("Bot####################################################################", reminder.title)

        message = f"Eslatma: {reminder.title}\n\n{reminder.content}"

        if reminder.user.telegram_id:
            bot.send_message(
                chat_id=reminder.user.telegram_id,
                text=message
            )

        reminder.status = 'completed'
        reminder.save()

    except Reminder.DoesNotExist:
        return f"Error {reminder_id} not"
