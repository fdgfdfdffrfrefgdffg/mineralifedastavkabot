from aiogram.fsm.state import State, StatesGroup

class Login(StatesGroup):
    login = State()
    parol = State()
    