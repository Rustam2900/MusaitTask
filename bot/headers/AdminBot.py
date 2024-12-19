from aiogram import Router, F, Bot
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, ReplyKeyboardRemove
from django.conf import settings

from bot.db import get_user_statistics, get_all_users
from bot.keyboards import get_main_menu, get_admin_menu
from bot.models import User
from bot.states import SendMessage

router = Router()
bot = Bot(token=settings.BOT_TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))


# -------------------------------------->   Add Movie   <------------------------------------------- #


@router.message(Command('admin'))
async def admin(message: Message):
    user_id = message.from_user.id

    user = await User.objects.filter(telegram_id=user_id).afirst()
    main_menu_markup = get_main_menu()
    admin_menu_markup = get_admin_menu()
    if user_id == 6736873215:
        await message.answer(text="👮🏻‍♂️Admin Xushkelibsiz\n"
                                  "Iltimos, quyidagi buyruqlardan birini tanlang:", reply_markup=admin_menu_markup)
    else:
        await message.answer(text="👮🏻‍♂️Uzur siz Admin emassiz", reply_markup=main_menu_markup)


@router.message(F.text == "👤Statistika")
async def show_statistics(message: Message):
    user_id = message.from_user.id
    if user_id == 6736873215:
        user_stats = await get_user_statistics()

        statistics = f"👤 Foydalanuvchilar:\n" \
                     f"24 soatda yangi foydalanuvchilar: {user_stats['new_users_24h']}\n" \
                     f"1 oyda yangi foydalanuvchilar: {user_stats['new_users_1_month']}\n" \
                     f"Jami foydalanuvchilar: {user_stats['total_users']}\n\n"

        await message.answer(text=statistics)
    else:
        await message.answer(
            text="Siz admin emassiz, statistikani ko'rish huquqiga ega emassiz.",
            reply_markup=None
        )


@router.message(F.text == "✍️ Habar yuborish")
async def send_message_users(message: Message, state: FSMContext):
    if message.from_user.id == 6736873215:
        await state.set_state(SendMessage.msg)
        await message.answer(text='Reklama xabarini yuboring!', reply_markup=ReplyKeyboardRemove())
    else:
        await message.answer('Sizga bu buyruqdan foydalana olmaysiz')


@router.message(SendMessage.msg)
async def send_message(message: Message, state: FSMContext):
    await state.clear()
    users = await get_all_users()
    total_users = len(users)
    failed_count = 0

    for user in users:
        try:
            await bot.forward_message(
                chat_id=user.telegram_id,
                from_chat_id=message.from_user.id,
                message_id=message.message_id,
            )
        except Exception:
            failed_count += 1

    sent_count = total_users - failed_count
    await bot.send_message(
        chat_id=6736873215,
        text=(
            f"<b>Bot a'zolari soni:</b> {total_users}\n"
            f"<b>Yuborilmadi:</b> {failed_count}\n"
            f"<b>Yuborildi:</b> {sent_count}"
        ),
        parse_mode=ParseMode.HTML,
    )
