from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login
from django.contrib import messages
from django.urls import reverse
from bot.forms import RegistrationForm, ReminderForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required

from bot.models import Reminder
from django.core.paginator import Paginator


def register(request):
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Siz ro'yxatdan o'tdingiz")
            return redirect(reverse('reminder_list'))
        else:
            messages.error(request, "error")
    else:
        form = RegistrationForm()
    return render(request, 'register.html', {'form': form})


def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})


@login_required
def reminder_list(request):
    reminders = Reminder.objects.filter(user=request.user).order_by('-date')

    paginator = Paginator(reminders, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'reminder_list.html', {'page_obj': page_obj})


@login_required
def add_reminder(request):
    if request.method == 'POST':
        form = ReminderForm(request.POST)
        if form.is_valid():
            reminder = form.save(commit=False)
            reminder.user = request.user
            reminder.save()
            return redirect('reminder_list')
    else:
        form = ReminderForm()
    return render(request, 'add_reminder.html', {'form': form})


@login_required
def edit_reminder(request, pk):
    reminder = get_object_or_404(Reminder, pk=pk, user=request.user)

    if request.method == 'POST':
        form = ReminderForm(request.POST, instance=reminder)
        if form.is_valid():
            form.save()
            return redirect('reminder_list')
    else:
        form = ReminderForm(instance=reminder)

    title = 'Eslatmani Tahrirlash' if reminder else 'Yangi Eslatma Qo\'shish'

    return render(request, 'edit_reminder.html', {'form': form, 'title': title})


def delete_reminder(request, id):
    reminder = get_object_or_404(Reminder, id=id)
    reminder.delete()
    return redirect('reminder_list')
