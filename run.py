# program 'test'
import asyncio

from aiogram import Bot, Dispatcher, F
from aiogram.filters import CommandStart, Command
from aiogram.types import Message

from config import TOKEN


bot = Bot(token=TOKEN)
dp = Dispatcher()


@dp.message(CommandStart())
async def cmd_start(message: Message):
    await message.reply(f'Привет.\nТвой ID: {message.from_user.id}\nИмя: {message.from_user.first_name}')


@dp.message(Command('help'))
async def get_help(message: Message):
    await message.answer('Это комманда /help')


@dp.message(F.text == 'Как дела?')
async def how_are_you(message: Message):
    await message.answer('OK!')


@dp.message(Command('get_photo'))
async def get_photo(message:Message):
    await message.answer_photo(photo='AgACAgIAAxkBAAMaZ3bj-cYhIFGh_C3QI6JzqCQpipkAApjqMRtUSLlL8Gc1RuQwxzMBAAMCAAN5AAM2BA', caption='Игрушка')


@dp.message(F.photo)
async def get_photo(message: Message):
    await message.answer(f'ID фото: {message.photo[-1].file_id}')


async def main():
    await dp.start_polling(bot)


if __name__ == '__main__':
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print('Exit')
