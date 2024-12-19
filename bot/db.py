from asgiref.sync import sync_to_async
from django.db.utils import IntegrityError
from django.contrib.auth.hashers import make_password
from bot.models import User


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
