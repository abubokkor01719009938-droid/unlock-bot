import logging
from aiogram import Bot, Dispatcher, executor, types

API_TOKEN = "8382275285:AAG0pKewuaNBcovrUOkzX_BlJsLpyMm-dNU"

logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    await message.reply("👋 হ্যালো! আমি আপনার আর্নিং বট।")

@dp.message_handler(commands=['help'])
async def send_help(message: types.Message):
    await message.reply("ℹ️ কমান্ডসমূহ:\n/start - শুরু করুন\n/help - হেল্প দেখুন")

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
