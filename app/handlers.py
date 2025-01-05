from aiogram import F, Router
from aiogram.filters import CommandStart, Command
from aiogram.types import Message

import app.keyboards as kb

router = Router()


@router.message(CommandStart())
async def cmd_start(message: Message):
    await message.reply(f'Привет.\nТвой ID: {message.from_user.id}\nИмя: {message.from_user.first_name}', reply_markup=kb.settings)


@router.message(Command('help'))
async def get_help(message: Message):
    await message.answer('Это комманда /help')


@router.message(F.text == 'Как дела?')
async def how_are_you(message: Message):
    await message.answer('OK!')


@router.message(Command('get_photo'))
async def get_photo(message:Message):
    await message.answer_photo(photo='AgACAgIAAxkBAAMaZ3bj-cYhIFGh_C3QI6JzqCQpipkAApjqMRtUSLlL8Gc1RuQwxzMBAAMCAAN5AAM2BA', caption='Игрушка')


@router.message(F.photo)
async def get_photo(message: Message):
    await message.answer(f'ID фото: {message.photo[-1].file_id}')
