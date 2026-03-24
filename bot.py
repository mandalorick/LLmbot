from olama.main import User_chat_Ollama

from aiogram import Bot, Dispatcher, types
from aiogram.filters.command import Command

import asyncio
import logging

from config import BOT_TOKEN
import os
os.environ["NO_PROXY"] = "127.0.0.1,localhost"

users = dict()

logging.basicConfig(level=logging.INFO)


bot = Bot(token=BOT_TOKEN)

dp = Dispatcher()


@dp.message(Command("clear"))
async def cmd_start(message: types.Message):
    if str(message.from_user.id) in users:
        users[str(message.from_user.id)].clear_chat_user()
        await message.answer("Твой чат был очищен!")
    else:
        await message.answer("Твой чат и так чист!")

@dp.message()
async def echo_handler(message: types.Message):
    user_id = message.from_user.id
    if str(message.from_user.id) not in users:
        users[str(message.from_user.id)] = User_chat_Ollama()
    await message.answer(users[str(message.from_user.id)].add_question(message.text))


async def main():
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
