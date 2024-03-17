from aiogram import Bot, Dispatcher, types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils import executor

API_TOKEN = "6942672775:AAEVeY6UM5h8rcLX8lpwZxMKP3_JQhHtZ6U"

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


# "Start" tugmasini yaratish
@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    keyboard = InlineKeyboardMarkup()
    keyboard.add(InlineKeyboardButton('Next', callback_data='next'))
    await message.reply("Press 'Next' to go to the next step:", reply_markup=keyboard)


# "Next" tugmasi bosilganda keyingi tugmani ochish
@dp.callback_query_handler(lambda c: c.data == 'next')
async def next_step(callback_query: types.CallbackQuery):
    await callback_query.answer()
    await bot.send_message(callback_query.from_user.id, "You pressed the 'Next' button.")
    keyboard = InlineKeyboardMarkup()
    keyboard.add(InlineKeyboardButton('Another Button', callback_data='another'))
    await bot.send_message(callback_query.from_user.id, "Press 'Another Button' now:", reply_markup=keyboard)


# "Another Button" tugmasi bosilganda bir nechta javob
@dp.callback_query_handler(lambda c: c.data == 'another')
async def another_button(callback_query: types.CallbackQuery):
    await callback_query.answer()
    await bot.send_message(callback_query.from_user.id, "You pressed the 'Another Button'.")


# Botni ishga tushirish
if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)