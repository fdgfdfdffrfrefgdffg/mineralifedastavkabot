from aiogram.types import Message
from aiogram.fsm.context import FSMContext
from api_requests import get_autos
import states
import keyboards.reply as reply_kb
from sqldata import add_user

async def start_yes(message: Message):
    await message.answer("Nima qilamiz?", reply_markup=reply_kb.main_menu)

async def start_no(message: Message, state: FSMContext):
    await message.answer("Assalomu alaykum, login kiriting.")
    await state.set_state(states.Login.login)

async def input_login(message: Message, state: FSMContext):
    autolar = await get_autos()
    for i in autolar:
        if i["login"] == message.text:
            await message.answer("Login topildi. Parol kiriting.")
            await state.set_state(states.Login.parol)
            await state.update_data(parol=i["parol"])
            await state.update_data(login=i["login"])

            return

    await message.answer("Login topilmadi!")

async def input_password(message: Message, state: FSMContext):
    context = await state.get_data()
    if context["parol"] == message.text:
        add_user(message.from_user.id, context["login"], context["parol"])
        await message.answer("Parol to'g'ri! Siz tizimga kirdingiz!", reply_markup=reply_kb.main_menu)
        await state.clear()
    else:
        await message.answer("Parol noto'g'ri!")