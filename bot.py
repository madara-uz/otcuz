import asyncio
from aiogram import Bot, Dispatcher
from data.config import BOT_TOKEN
from handlers import start
from database.db import create_tables

async def main():
    create_tables()
    bot = Bot(token=BOT_TOKEN, parse_mode="HTML")
    dp = Dispatcher()
    dp.include_router(start.router)
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
