from django.contrib.auth import get_user_model
from django.test import TestCase
from bot import models
from django.utils import timezone


class UserModelTestCase(TestCase):
    def test_create_user(self):
        user = models.User.objects.create_user(
            email='Rustam@gmail.com',
            full_name='rustamali',
            username='alisher',
            phone_number='+998 90 000 00 00',
            telegram_id='123456',
            tg_username='test',
            password='password123'
        )
        self.assertEqual(models.User.objects.count(), 1)


# class ReminderModelsTestCase(TestCase):
#     def setUp(self):
#         self.user = get_user_model().objects.create_user(
#             email='Rustam1@gmail.com',
#             full_name='rustamali1',
#             username='alisher1',
#             phone_number='+998 90 000 00 01',
#             telegram_id='1234561',
#             tg_username='test1',
#             password='password1231'
#         )
#
#     def test_create_reminder(self):
#         reminder = models.Reminder.objects.create(
#             title='test',
#             content='test',
#             date=timezone.now(),
#             user=self.user,
#             status='Pending'
#         )
#         self.assertEqual(models.Reminder.objects.count(), 1)
