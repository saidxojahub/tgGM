from aiogram import types
from aiogram.types import WebAppInfo

web_app = WebAppInfo(url='https://gm-cars.netlify.app/')

keyboard = types.ReplyKeyboardMarkup(
    keyboard=[
        [types.KeyboardButton(text='🤩ɪɴᴛᴇʀᴀᴋᴛɪᴠ ᴍᴇɴʏᴜ', web_app=web_app)]
    ],
    resize_keyboard=True
)

