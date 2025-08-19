from aiogram import Router, F, Bot
from aiogram.types import Message, ReplyKeyboardMarkup, KeyboardButton
from aiogram.types import ReplyKeyboardRemove
from aiogram.filters import CommandStart
from database.db import add_user
from datetime import datetime

router = Router()

@router.message(CommandStart())
async def start_handler(message: Message):
    kb = ReplyKeyboardMarkup(
        keyboard=[[KeyboardButton(text="📱 Kontaktni ulashish", request_contact=True)]],
        resize_keyboard=True
    )
    await message.answer("Ro‘yxatdan o‘tish uchun telefon raqamingizni ulashing:", reply_markup=kb)

@router.message(F.contact)
async def contact_handler(message: Message, bot: Bot):
    contact = message.contact
    telegram_id = contact.user_id
    first_name = message.from_user.first_name
    phone = contact.phone_number
    registered_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    add_user(telegram_id, first_name, phone, registered_at)

    await message.answer(
        "✅ Siz muvaffaqiyatli ro‘yxatdan o‘tdingiz!",
        reply_markup=ReplyKeyboardRemove()
  )
  
