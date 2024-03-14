from database_bot import Database
import logging
import os
from dotenv import load_dotenv
from aiogram import Bot, Dispatcher, executor, types
from button import (menu_keyword, menu_inside, category_menu, types_menu, musics, videos, musics_category,
                    videos_category, inter_menu, fun_menu)
load_dotenv()

TOKEN = os.getenv('BOT_TOKEN')
logging.basicConfig(level=logging.INFO)

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    first_name = message.from_user.first_name
    last_name = message.from_user.last_name
    username = message.from_user.username
    chat_id = str(message.chat.id)
    check_data = f"""SELECT * FROM users_data WHERE chat_id = '{chat_id}';"""
    if len(Database.connect(check_data, 'select')) >= 1:
        await message.answer(f'Hello @{username}', reply_markup=menu_keyword)
        await bot.send_message(chat_id=chat_id, text=f"I am personal_data bot")
        await bot.send_message(chat_id=chat_id, text=f"send /data to me and I will send your information to you")
    else:
        query = f"""INSERT INTO users_data(first_name, last_name, username, chat_id) VALUES(
            '{first_name}',
             '{last_name}',
             '{username}',
             '{chat_id}');"""
        print(f"{username} {Database.connect(query, 'insert')}")
        await message.answer(f'Hello @{username}', reply_markup=menu_keyword)
        await bot.send_message(chat_id=chat_id, text=f"I am personal_data bot")
        await bot.send_message(chat_id=chat_id, text=f"send /data to me and I will send your information to you")


@dp.message_handler(commands=['data', ])
async def get_data(message: types.Message):
    chat_id = message.chat.id
    query = f"""SELECT * FROM users_data WHERE chat_id = '{chat_id}';"""
    data = Database.connect(query, 'select')
    print(data)
    if message.text == '/data':
        await message.reply(f"""
        Hi {data[0][3]}
        first_name: {data[0][1]}
        last_name: {data[0][2]}
        chat_id: {data[0][4]}""")
    else:
        await message.answer(f"I am not understand this message 🤷‍♂️")


@dp.message_handler(lambda message: message.text == 'Menu')
async def show_menu(message: types.Message):
    await message.answer("Menulardan birini tanlang:", reply_markup=menu_inside)


@dp.message_handler(lambda message: message.text in ['musics', 'videos'])
async def menu_ins(message: types.Message):
    if message.text == "musics":
        await message.answer('musics', reply_markup=musics)
    else:
        await message.answer('videos', reply_markup=videos)


@dp.message_handler(lambda message: message.text == 'Category')
async def show_category(message: types.Message):
    await message.answer("Categoriyalardan birini tanlang:", reply_markup=category_menu)


@dp.message_handler(lambda message: message.text in ['music category', 'video category'])
async def category_m(message: types.Message):
    if message.text == "music category":
        await message.answer('music category', reply_markup=musics_category)
    else:
        await message.answer('video category', reply_markup=videos_category)


@dp.message_handler(lambda message: message.text == 'Types')
async def show_types(message: types.Message):
    await message.answer("Qidirayotgan malumotingizni turini tanlang:", reply_markup=types_menu)


@dp.message_handler(lambda message: message.text in ['interesting', 'funny'])
async def types_m(message: types.Message):
    if message.text == "interesting":
        await message.answer('interesting', reply_markup=inter_menu)
    else:
        await message.answer('funny', reply_markup=fun_menu)


@dp.message_handler(lambda message: message.text == 'back')
async def back_x(message: types.Message):
    await message.answer("Menulardan birini tanlang:", reply_markup=menu_keyword)


@dp.message_handler(lambda message: message.text not in ["Menu", "Category", "Types", "videos", "musics", "back", "contacts",
                                                         "serial", "Ujas", "Detective", "Historical", "Yulduz Usmonova", "Bahrom Nazarov", "Jahongir Otajonov", "videos category", "musics category"
                                                         "interesting", "funny", "world films"])
async def invalid_message(message: types.Message):
    if message.text not in ["Menu", "Category", "Types", "videos", "musics", "back", "films", "contacts",
                                                         "serial", "Ujas", "Detective", "Historical", "Yulduz Usmonova", "Bahrom Nazarov", "Jahongir Otajonov", "videos category", "musics category"
                                                         "interesting", "funny", "world films"]:
        await message.answer("Invalid")

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)



