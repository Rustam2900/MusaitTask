# Generated by Django 4.2 on 2024-12-17 09:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bot', '0002_user_delete_customuser'),
    ]

    operations = [
        migrations.CreateModel(
            name='Reminder',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='title')),
                ('title_uz', models.CharField(max_length=255, null=True, verbose_name='title')),
                ('title_ru', models.CharField(max_length=255, null=True, verbose_name='title')),
                ('content', models.TextField(verbose_name='content')),
                ('content_uz', models.TextField(null=True, verbose_name='content')),
                ('content_ru', models.TextField(null=True, verbose_name='content')),
                ('date', models.DateTimeField()),
                ('status', models.CharField(choices=[('pending', 'Pending'), ('completed', 'Completed')], default='pending', max_length=20)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reminders', to='bot.user')),
            ],
            options={
                'verbose_name': 'Reminder',
                'verbose_name_plural': 'Reminders',
                'ordering': ['-date'],
            },
        ),
    ]
