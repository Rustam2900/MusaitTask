import re

from aiogram import Bot, Router
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, CallbackQuery

from bot.models import User
from bot.db import save_user_language
from bot.keyboards import get_languages, get_main_menu
from bot.states import UserStates

from bot.utils import default_languages, user_languages, introduction_template, \
    fix_phone
from django.conf import settings
from aiogram.client.default import DefaultBotProperties

router = Router()
bot = Bot(token=settings.BOT_TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))


@router.message(CommandStart())
async def welcome(message: Message):
    user_id = message.from_user.id

    user = await User.objects.filter(telegram_id=user_id).afirst()

    if user and user.user_lang:
        main_menu_markup = get_main_menu(user.user_lang)
        await message.answer(
            text=introduction_template[user.user_lang],
            reply_markup=main_menu_markup,
            parse_mode="HTML"
        )
    else:
        msg = default_languages['welcome_message']
        await message.answer(text=msg, reply_markup=get_languages(), parse_mode="HTML")


@router.callback_query(lambda call: call.data.startswith("lang"))
async def get_query_languages(call: CallbackQuery, state: FSMContext):
    user_id = call.from_user.id
    user_lang = call.data.split("_")[1]
    user_languages[user_id] = user_lang

    await save_user_language(user_id, user_lang)

    await bot.answer_callback_query(call.id)
    await state.set_state(UserStates.ID)

    text = default_languages[user_lang]['ID']
    await call.message.answer(text, reply_markup=None)


@router.message(UserStates.ID)
async def reg_user_contact(message: Message, state: FSMContext):
    user_id = message.from_user.id
    user_lang = user_languages.get(user_id, 'uz')

    input_id = message.text.strip()
    user = await User.objects.filter(generate_id=input_id).afirst()
    if user:
        full_name = user.full_name if user.full_name else message.from_user.username
        text = f"{user_lang.upper()}:\nXush kelibsiz, {full_name}!"
        await message.answer(text=text, reply_markup=get_main_menu(user_lang), parse_mode="HTML")
        await state.clear()
    else:
        error_text = default_languages[user_lang]['invalid_id']
        await message.answer(text=error_text, reply_markup=None, parse_mode="HTML")
