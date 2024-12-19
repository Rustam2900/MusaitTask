from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session
from bot.database.database import User
from django.contrib.auth.hashers import make_password


def add_user(user_data: dict):
    db = Session()
    try:
        new_user = User(
            email=user_data["email"],
            username=user_data.get("username"),
            phone_number=user_data["phone_number"],
            password=make_password(user_data["password"]),
            telegram_id=user_data["telegram_id"],
            tg_username=user_data.get("tg_username")
        )
        db.add(new_user)
        db.commit()
        db.refresh(new_user)
        return new_user
    except IntegrityError:
        db.rollback()
        return None
    finally:
        db.close()
