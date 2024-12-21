from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton


def get_main_menu():
    main_menu_keyboard = ReplyKeyboardMarkup(keyboard=[
        [
            KeyboardButton(text="Yangi eslatma add"),
            KeyboardButton(text="Eslatmalar ro'yxati")
        ],
        [
            KeyboardButton(text="Eslatmani delete"),
            KeyboardButton(text='Done')
        ],

    ], resize_keyboard=True)
    return main_menu_keyboard


def get_admin_menu():
    admin_menu_keyboard = ReplyKeyboardMarkup(keyboard=[
        [
            KeyboardButton(text="👤Statistika"),
            KeyboardButton(text="✍️ Habar yuborish")
        ],
        # [
        #     KeyboardButton(text="Admin add"),
        #     KeyboardButton(text="Admin delete")
        # ]

    ], resize_keyboard=True)
    return admin_menu_keyboard


def get_registration_and_login_keyboard():
    registration_keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text='registration', callback_data='registration')],
        [InlineKeyboardButton(text='login', callback_data='login')], ])

    return registration_keyboard if registration_keyboard else []
