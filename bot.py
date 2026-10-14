import asyncio
import logging
import os
from aiogram import Bot, Dispatcher
import google.generativeai as genai

TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

genai.configure(api_key=GEMINI_API_KEY)
model = genai.GenerativeModel('gemini-1.5-flash')

bot = Bot(token=TELEGRAM_TOKEN)
dp = Dispatcher()

@dp.message()
async def send_ai_response(message):
    await bot.send_chat_action(message.chat.id, 'typing')
    try:
        response = model.generate_content(message.text)
        await message.answer(response.text)
    except Exception as e:
        await message.answer(f"Ошибка: {str(e)}")

async def main():
    logging.basicConfig(level=logging.INFO)
    print("Бот запущен!")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
