from aiogram import Bot, Dispatcher, executor, types
import logging
import requests

logging.basicConfig(level=logging.INFO)

bot = Bot(token="5904607271:AAH-edy50mxak7BhgfeCB-9oLnlrK5QMPiM")
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    await message.answer(f"Salom {message.from_user.full_name}")

@dp.message_handler()
async def echo(message: types.Message):
    pass

if __name__ == '__main__':
    executor.start_polling(dp)