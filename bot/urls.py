from django.urls import path
from bot.views import register, user_login, reminder_list, add_reminder, edit_reminder, delete_reminder

urlpatterns = [
    path('register/', register, name='register'),
    path('login/', user_login, name='login'),
    path('reminder_list/', reminder_list, name='reminder_list'),
    path('reminders/', reminder_list, name='reminder_list'),
    path('reminder/add/', add_reminder, name='add_reminder'),
    path('reminder/edit/<int:pk>/', edit_reminder, name='edit_reminder'),
    path('reminder/delete/<int:id>/', delete_reminder, name='delete_reminder'),

]
