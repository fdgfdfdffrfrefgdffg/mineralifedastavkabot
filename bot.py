from aiogram import Bot, Dispatcher
from asyncio import run
import config
import logging
import sqldata
import message

dp = Dispatcher()

async def main():
    bot = Bot(token=config.token)
    logging.basicConfig(level=logging.INFO)
    dp.include_router(message.router)
    await dp.start_polling(bot)
    sqldata.close_db()

run(main())
