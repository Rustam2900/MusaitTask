from aiogram.fsm.state import State, StatesGroup


class UserRegisterStates(StatesGroup):
    email = State()
    username = State()
    phone_number = State()
    parol = State()


class UserLoginStates(StatesGroup):
    username = State()
    parol = State()


class SendMessage(StatesGroup):
    msg = State()


class ReminderStates(StatesGroup):
    title = State()
    content = State()
    date = State()
