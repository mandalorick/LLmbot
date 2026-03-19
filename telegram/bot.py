from olama.main import User_chat_Ollama

from aiogram import Bot, Dispatcher, types
from aiogram.filters.command import Command

import asyncio
import logging

from config import BOT_TOKEN

# ВАЖНО! Вставьте сюда ваш токен, полученный от @BotFather


# Включаем логирование, чтобы не пропустить важные сообщения
logging.basicConfig(level=logging.INFO)

# Объект бота
bot = Bot(token=BOT_TOKEN)
# Диспетчер
dp = Dispatcher()
#
# # Хэндлер на команду /start
# @dp.message(Command("start"))
# async def cmd_start(message: types.Message):
#     await message.answer("Привет! Я эхо-бот. Отправь мне любое сообщение, и я его повторю.")

# Хэндлер на остальные текстовые сообщения
@dp.message()
async def echo_handler(message: types.Message):
    user = User_chat_Ollama()
    await message.answer(user.add_question(message.text))

# Запуск процесса поллинга новых апдейтов
async def main():
    # Удаляем вебхук и пропускаем накопившиеся входящие сообщения
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
