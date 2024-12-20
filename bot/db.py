from datetime import timedelta
from django.utils import timezone

from asgiref.sync import sync_to_async
from django.db.utils import IntegrityError

from bot.models import User, Reminder


@sync_to_async
def create_user_db(user_data):
    user_data['phone_number'] = user_data['phone_number'].replace(" ", "").strip()
    try:
        new_user = User.objects.create(**user_data)
        print("####################")
        print(new_user)
        print("####################")
        return new_user
    except IntegrityError:
        raise Exception("User already exists")


@sync_to_async
def is_email_exists(email):
    return User.objects.filter(email=email).exists()


@sync_to_async
def is_phone_exists(phone_number):
    phone_number = phone_number.replace(" ", "").strip()

    return User.objects.filter(phone_number=phone_number).exists()


async def get_user_telegram_id(telegram_id):
    return await User.objects.filter(telegram_id=telegram_id).afirst()


@sync_to_async
def get_user_username(username):
    return User.objects.filter(username=username).first()


@sync_to_async
def update_telegram_info(user, user_data):
    try:
        user.telegram_id = user_data.get("telegram_id")
        user.full_name = user_data.get("full_name")
        user.tg_username = user_data.get("tg_username")
        user.save()
        return user
    except IntegrityError as e:
        raise Exception(f"Error occurred while updating user: {e}")


@sync_to_async
def get_user_statistics():
    total_users = User.objects.count()

    time_24_hours_ago = timezone.now() - timedelta(days=1)
    new_users_24h = User.objects.filter(create_at__gte=time_24_hours_ago).count()

    time_1_month_ago = timezone.now() - timedelta(days=30)
    new_users_1_month = User.objects.filter(create_at__gte=time_1_month_ago).count()

    return {
        "total_users": total_users,
        "new_users_24h": new_users_24h,
        "new_users_1_month": new_users_1_month
    }


@sync_to_async
def get_all_users():
    return list(User.objects.all())


@sync_to_async
def get_user_by_telegram_id_sync(telegram_id: int):
    user = User.objects.filter(telegram_id=telegram_id).first()
    return user


async def get_user_by_telegram_id(telegram_id: int):
    user = await get_user_by_telegram_id_sync(telegram_id)
    if user:
        return user
    else:
        user_data = {
            'telegram_id': telegram_id,
        }
        return await create_user_db(user_data)


@sync_to_async
def reminder_add_db(reminder_data):
    try:
        reminder_new = Reminder.objects.create(**reminder_data)
        print("####################")
        print(reminder_new)
        print("####################")
        return reminder_new
    except IntegrityError:
        raise Exception("User already exists")
