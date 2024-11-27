import asyncio
import logging
from aiogram import Bot, Dispatcher, F
from aiogram import types
from aiogram.filters.command import Command
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from root import TOKEN
from aiogram import Bot, types
from aiogram.types import LabeledPrice, PreCheckoutQuery
from keyboards import keyboard

dp = Dispatcher()

@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    await message.answer(f"ᴀssᴀʟᴀᴍᴜ ᴀʟᴇʏᴋᴜᴍ!\nʏᴀɴɢɪ ᴠᴀ ǫᴜʟᴀʏ ᴍᴇɴʏᴜ ᴏʀǫᴀʟɪ ʙᴜʏᴜʀᴛᴍᴀ ʙᴇʀɪɴɢ👇😉",
                         reply_markup=keyboard)
async def main() -> None:
    bot = Bot(token=TOKEN)
    await dp.start_polling(bot)


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())
