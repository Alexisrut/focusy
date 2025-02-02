import logging
from aiogram import Bot, Dispatcher, types, F
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State
from aiogram.types import InlineKeyboardMarkup, WebAppInfo, InlineKeyboardButton

from sqlalchemy import ForeignKey, Column, BigInteger, String, DateTime, Boolean
from typing import List
from sqlalchemy.ext.asyncio import create_async_engine, AsyncAttrs, async_sessionmaker
from datetime import datetime
from requests import add_user
from models import async_session

# Set up logging
logging.basicConfig(level=logging.INFO)
BOT_TOKEN = '8158341812:AAHyragguB3-u2uIYjfqYuH7g5burb551c0'
# Initialize bot and dispatcher
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

# Create database when bot starts
# States
class Form(StatesGroup):
    name = State()
    year = State()

# Start command handler
@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    # Create reply keyboard with one button
    keyboard = types.ReplyKeyboardMarkup(
        keyboard=[
            [types.KeyboardButton(text="Готов!")]
        ],
        resize_keyboard=True
    )
    
    await message.answer(
        "Привет! Меня зовут Focusy, ваш помошник по подготовке к ЕГЭ, готовы стать на шаг ближе к сотке?",
        reply_markup=keyboard
    )

# Handle button click
@dp.message(F.text == "Готов!")
async def start_registration(message: types.Message, state: FSMContext):
    await message.answer("Как мне к тебе обращаться", reply_markup=types.ReplyKeyboardRemove())
    await state.set_state(Form.name)

# Handle name input
@dp.message(Form.name)
async def process_name(message: types.Message, state: FSMContext):
    await state.update_data(name=message.text)
    user_data = await state.get_data()
    await message.answer(f"{user_data['name']}, в каком классе вы учитесь?")
    await state.set_state(Form.year)

# Handle phone number input
@dp.message(Form.year)
async def process_year(message: types.Message, state: FSMContext):
    user_data = await state.get_data()
    
    # Save to database
    await add_user(
        tg_id=message.from_user.id,
        name=user_data['name'],
        year=message.text
    )

    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(
            text="Open Mini App", 
            web_app=WebAppInfo(url='https://focus-c6088.web.app')
        )]
    ])

    await message.answer(
        "Отлично! Заходи быстрее в приложение и мы начнём👇",
        reply_markup=keyboard
    )
    await state.clear()

# Run the bot
if __name__ == "__main__":
    import asyncio
    asyncio.run(dp.start_polling(bot))