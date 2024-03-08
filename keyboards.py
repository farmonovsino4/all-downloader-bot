from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove

lang_button = ReplyKeyboardMarkup(row_width=1, resize_keyboard=True).add(
    KeyboardButton(text='🇺🇸English'),
    KeyboardButton(text='🇷🇺Русский'),
    KeyboardButton(text='🇺🇿Uzbek')
)