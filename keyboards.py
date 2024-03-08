from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

lang_button = ReplyKeyboardMarkup(row_width=1, resize_keyboard=True).add(
    KeyboardButton(text='🇺🇸English', callback_data='en'),
    KeyboardButton(text='🇷🇺Русский', callback_data='ru'),
    KeyboardButton(text='🇺🇿Uzbek', callback_data='uz')
)