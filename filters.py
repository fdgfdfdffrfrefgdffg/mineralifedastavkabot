from aiogram.filters import Filter
from aiogram.types import Message
from sqldata import get_user

class UserCheck(Filter):
    async def __call__(self, message: Message):
        return not bool(get_user(message.from_user.id))
