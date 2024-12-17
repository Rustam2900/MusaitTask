from aiogram import Router, Bot
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.filters import Command
from aiogram.types import Message
from django.conf import settings


router = Router()
bot = Bot(token=settings.BOT_TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))


# -------------------------------------->   Add Movie   <------------------------------------------- #


@router.message(Command('admin'))
async def admin(message: Message):
    await message.answer("Hello Admin")
