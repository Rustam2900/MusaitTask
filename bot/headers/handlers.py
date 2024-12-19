from aiogram import Bot, Router, F
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, CallbackQuery

from bot.db import create_user_db, is_email_exists, is_phone_exists, \
    get_user_username, get_user_telegram_id, update_telegram_info
from bot.keyboards import get_main_menu, get_registration_and_login_keyboard
from bot.states import UserRegisterStates, UserLoginStates
from django.contrib.auth.hashers import make_password, check_password
from bot.validators import validate_email, phone_number_validator, validate_password
from django.conf import settings
from aiogram.client.default import DefaultBotProperties
from aiogram.utils.text_decorations import html_decoration as fmt
from django.core.exceptions import ValidationError

router = Router()
bot = Bot(token=settings.BOT_TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))


@router.message(CommandStart())
async def welcome(message: Message):
    user_id = message.from_user.id

    user = await get_user_telegram_id(user_id)

    if user:
        main_menu_markup = get_main_menu()
        await message.answer(
            text="Buyruqlardan birortasini tanlang:",
            reply_markup=main_menu_markup,
            parse_mode="HTML"
        )
    else:
        await message.answer(
            text="Ro'yxatdan o'ting yoki tizimga kiring:",
            reply_markup=get_registration_and_login_keyboard(),
            parse_mode="HTML"
        )


@router.callback_query(F.data == "registration")
async def reg_user_contact(call: CallbackQuery, state: FSMContext):
    await call.message.answer(text="Iltimos Emailliz kiriting")
    await state.set_state(UserRegisterStates.email)


@router.message(UserRegisterStates.email)
async def reg_user_email(message: Message, state: FSMContext):
    email = message.text.strip()

    if not validate_email(email):
        await message.answer(
            "Email manzilingiz noto'g'ri formatda. Iltimos, quyidagiga o'xshash formatda kiritishingiz kerak:\n"
            f"{fmt.pre('example@gmail.com')}"
        )
        return

    if await is_email_exists(email):
        await message.answer("Bu email manzili allaqachon ro'yxatdan o'tgan. Iltimos, boshqa email manzil kiriting.")
        return

    await state.update_data(email=email)
    await message.answer("Email qabul qilindi! Endi iltimos foydalanuvchi nomingizni kiriting:")
    await state.set_state(UserRegisterStates.username)


@router.message(UserRegisterStates.username)
async def reg_user_username(message: Message, state: FSMContext):
    await state.update_data(username=message.text)
    await message.answer("Iltimos, telefon raqamingizni kiriting:")
    await state.set_state(UserRegisterStates.phone_number)


@router.message(UserRegisterStates.phone_number)
async def reg_user_phone_number(message: Message, state: FSMContext):
    phone_number = message.text.strip()

    try:
        phone_number_validator(phone_number)
    except ValidationError:
        await message.answer(
            "Telefon raqami manzilingiz noto'g'ri formatda. "
            "Iltimos, quyidagiga o'xshash formatda kiritishingiz kerak:\n"
            f"{fmt.pre('+998XX XXX XX XX')}"
        )
        return

    if await is_phone_exists(phone_number):
        await message.answer(
            "Bu telefon raqami manzili allaqachon ro'yxatdan o'tgan. Iltimos, boshqa telefon raqamini kiriting.")
        return

    await state.update_data(phone_number=phone_number)
    await message.answer("Iltimos, parolingizni kiriting:")
    await state.set_state(UserRegisterStates.parol)
    await state.set_state(UserRegisterStates.parol)


@router.message(UserRegisterStates.parol)
async def reg_user_save(message: Message, state: FSMContext):
    password = message.text
    if not validate_password(password):
        await message.answer("Parol kamida 8 belgidan iborat bo'lishi kerak. Iltimos, qaytadan kiriting.")
        return

    user_data = await state.get_data()
    user_data['password'] = make_password(password)
    user_data['telegram_id'] = message.from_user.id
    user_data['tg_username'] = message.from_user.username
    user_data['full_name'] = message.from_user.full_name

    try:
        result = await create_user_db(user_data)
        if result:
            await message.answer("Ro'yxatdan o'tish muvaffaqiyatli yakunlandi!", reply_markup=get_main_menu())
        else:
            await message.answer("Bu email yoki telefon raqami avval ro'yxatdan o'tgan!")
    except Exception as e:
        await message.answer("Xatolik yuz berdi: {}".format(str(e)))

    await state.clear()


@router.callback_query(F.data == "login")
async def user_sign_in(call: CallbackQuery, state: FSMContext):
    await state.set_state(UserLoginStates.username)
    await call.message.answer(text="Iltimos, foydalanuvchi nomingizni kiriting:")


@router.message(UserLoginStates.username)
async def get_username(message: Message, state: FSMContext):
    await state.update_data(username=message.text)
    await state.set_state(UserLoginStates.parol)
    await message.answer(text="Iltimos, parolingizni kiriting:")


@router.message(UserLoginStates.parol)
async def get_password(message: Message, state: FSMContext):
    user_data = await state.get_data()
    username = user_data.get("username")
    password = message.text

    user = await get_user_username(username)

    if user:
        if check_password(password, user.password):
            user_data_to_save = {
                "telegram_id": message.from_user.id,
                "full_name": message.from_user.full_name,
                "tg_username": message.from_user.username,
            }

            user = await update_telegram_info(user, user_data_to_save)

            await state.clear()
            await message.answer(
                text="Tizimga muvaffaqiyatli kirdingiz! Asosiy menyu:",
                reply_markup=get_main_menu(),
            )
        else:
            await message.answer(text="Parol noto‘g‘ri. Qaytadan urinib ko‘ring!")
    else:
        await message.answer(
            text="Bunday foydalanuvchi mavjud emas. Iltimos, qaytadan tekshiring yoki register qiling!")
        await state.clear()

