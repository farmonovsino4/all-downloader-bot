from aiogram import Bot, Dispatcher, executor, types
import logging
from downloader import TikTokdDownloader, FacebookDownloader
import requests
from pytube import YouTube
import os
from environs import Env
from keyboards import lang_button, ReplyKeyboardRemove

logging.basicConfig(level=logging.INFO)

env = Env()
env.read_env()

bot = Bot(token=env.str('TOKEN'))
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    msg = await message.answer("choose language | tilni tanlang | выберите язык", reply_markup=lang_button)

@dp.message_handler()
async def lang(message: types.Message):
    if message.text == 'en':
        await message.answer(f"Hello <b>{message.from_user.first_name}</b>\i'm downloader bot\ni can download video from <b>instagram, tiktok, facebook, youtube</b>", parse_mode='html', reply_markup=ReplyKeyboardRemove())
    elif message.text == 'ru':
        await message.answer(f"Здравствуйте, <b>{message.from_user.first_name}</b>\я бот-загрузчик\nя могу скачивать видео с <b>instagram, tiktok, facebook, youtube</b>", parse_mode='html', reply_markup=ReplyKeyboardRemove())
    else:
        await message.answer(f"Salom, <b>{message.from_user.first_name}</b>\men video yuklovchi botman\nmen <b>instagram, tiktok, facebook, youtube</b>dan video yuklayolaman", parse_mode='html', reply_markup=ReplyKeyboardRemove())

@dp.message_handler()
async def echo(message: types.Message):
    if message.text.startswith('https://www.instagram.com/') or message.text.startswith('https://instagram.com/'):
        await message.answer("Yuklanmoqda")
        try:
            response = requests.get(f"https://u11843.xvest5.ru/api/instagram/v1?url={message.text}")
            await message.answer_video(video=response.json()['medias'][0]['url'])
        except Exception as e:
            await message.answer('Videoni yuklayolmadim')
            await bot.send_message(chat_id=5230484991, text=e)
    elif message.text.startswith('https://www.tiktok.com/') or message.text.startswith('https://tiktok.com/') or message.text.startswith('https://vt.tiktok.com/') or message.text.startswith('https://www.vt.tiktok.com/'):
        try:
            video = TikTokdDownloader(message.text)
            await message.answer("Yuklanmoqda")
            await message.answer_video(video=video['url'], caption=video['title'])
        except Exception as e:
            await message.answer('Videoni yuklayolmadim')            
            await bot.send_message(chat_id=5230484991, text=e)
    elif message.text.startswith('https://www.facebook.com/') or message.text.startswith('https://facebook.com/') or message.text.startswith('https://fb.watch/') or message.text.startswith('https://www.fb.watch/'):
        try:
            await message.answer("Yuklanmoqda")
            video = FacebookDownloader(message.text)
            await message.answer_video(video=video['url'], caption=video['title'])
        except Exception as e:
            await message.answer('Videoni yuklayolmadim')
            await bot.send_message(chat_id=5230484991, text=e)
    elif message.text.startswith('https://www.youtube.com/') or message.text.startswith('https://youtube.com/') or message.text.startswith('https://youtu.be/') or message.text.startswith('https://www.youtu.be/'):
        try:
            yt = YouTube(message.text)
            await message.answer('Yuklanmoqda')
            downloaded = yt.streams.filter(resolution='720p', file_extension='mp4', progressive=True).first().download()
            with open(str(downloaded), 'rb') as video:
                await message.answer_video(video=video, caption=yt.title)
        except Exception as e:
            await message.answer('Videoni yuklayolmadim')
            await bot.send_message(chat_id=5230484991, text=e)
        try:
            os.remove(str(downloaded))
        except:
            pass


if __name__ == '__main__':
    executor.start_polling(dp)