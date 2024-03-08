from aiogram import Bot, Dispatcher, executor, types
import logging
from downloader import instagram_downloader
import requests

logging.basicConfig(level=logging.INFO)

bot = Bot(token="5904607271:AAH-edy50mxak7BhgfeCB-9oLnlrK5QMPiM")
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    await message.answer(f"Salom {message.from_user.full_name}")

@dp.message_handler()
async def echo(message: types.Message):
    if message.text.startswith('https://www.instagram.com/') or message.text.startswith('https://instagram.com/'):
        await message.answer("Yuklanmoqda")
        try:
            response = requests.get(f"https://u11843.xvest5.ru/api/instagram/v1?url={message.text}")
            await message.answer_video(video=response.json()['medias'][0]['url'])
        except Exception as e:
            await bot.send_message(chat_id=5230484991, text=e)
    elif message.text.startswith('https://www.youtube.com/') or message.text.startswith('https://youtube.com/') or message.text.startswith('https://youtu.be/') or message.text.startswith('https://www.youtu.be/'):
        pass
@dp.message_handler(commands=['help'])
async def help(message: types.Message):
    await message.answer("Sizning chatingizga Instagram-da jo'natilgan videolarni yuklab olishingiz mumkin. Siz bu botga Instagram-da jo'natilgan video manzili yuboring va bot sizga video yuklaydi. Masalan: https://www.instagram.com/p/B-nQ0J1l36c/")


if __name__ == '__main__':
    executor.start_polling(dp)