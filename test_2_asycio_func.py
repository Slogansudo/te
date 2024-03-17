
from database_bot import Database
import logging
import os
from dotenv import load_dotenv
from aiogram.utils import executor
from aiogram import Bot, Dispatcher, executor, types
from inline_button import keyboard, musics, videos, category, musics_category, videos_category
from button import menu_keyword, services, add_musics
import time

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
        await bot.send_photo(message.chat.id, photo="https://coinvoice-international.oss-cn-hongkong.aliyuncs.com/profital-prod/article/20230929/2023092923033417957175.png", caption="I am personal_data bot")
    else:
        query = f"""INSERT INTO users_data(first_name, last_name, username, chat_id) VALUES(
            '{first_name}', '{last_name}', '{username}', '{chat_id}');"""
        print(f"{username} {Database.connect(query, 'insert')}")
        await message.answer(f'Hello @{username}', reply_markup=menu_keyword)
        await bot.send_photo(message.chat.id, photo="https://coinvoice-international.oss-cn-hongkong.aliyuncs.com/profital-prod/article/20230929/2023092923033417957175.png", caption="I am personal_data bot")


@dp.callback_query_handler(lambda c: c.data in ['Jaloliddin Axmadaliyev', 'Yulduz Usmonova', "Baxrom Nazarov"])
async def send_music(callback_query: types.CallbackQuery):
    query = f"""SELECT * FROM musics WHERE author_name = '{callback_query.data}';"""
    for i in Database.connect(query, 'select'):
        time.sleep(0.2)
        await bot.send_audio(callback_query.from_user.id, audio=i[2], caption=None)
    await bot.send_message(callback_query.from_user.id, 'call musics mission complete')


@dp.callback_query_handler(lambda c: c.data in ['serial', 'film', "short videos"])
async def send_video(callback_query: types.CallbackQuery):
    query = f"""SELECT * FROM videos WHERE name = '{callback_query.data}';"""
    for i in Database.connect(query, 'select'):
        time.sleep(0.2)
        await bot.send_video(callback_query.from_user.id, video=i[2], caption=None)
    await bot.send_message(callback_query.from_user.id, 'call videos mission complete')


@dp.message_handler(commands=['data'])
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


@dp.message_handler(commands=['image'])
async def send_image(message: types.Message):
    photo_url = 'https://www.freecodecamp.org/news/content/images/2021/08/chris-ried-ieic5Tq8YMk-unsplash.jpg'
    caption = 'photo'
    await bot.send_photo(message.chat.id, photo=photo_url, caption=caption)


@dp.message_handler(commands=['admin'])
async def admin_command(message: types.Message):
    query1 = f"SELECT * FROM users_data WHERE chat_id = '{message.from_user.id}';"
    query = "SELECT * FROM users_data WHERE status = true;"
    data_x = Database.connect(query1, 'select')
    data = Database.connect(query, 'select')
    if data_x[0] in data:
        await message.reply("Salom admin")
        await message.reply(text="qaysi servisni o'zgartirishni hohlaysiz", reply_markup=services)
    else:
        await message.reply("Bunday buyruq turi mavjud emas")


@dp.message_handler(lambda message: message.text == ['add_musics', 'add videos', 'change_admins', 'back'])
async def admin_change(message: types.Message):
    query = "SELECT * FROM users_data WHERE status = true;"
    query_2 = f"SELECT * FROM users_data WHERE chat_id = '{message.from_user.id}';"
    data_1 = Database.connect(query, 'select')
    data_2 = Database.connect(query_2, 'select')
    if data_2[0] in data_1:
        if message.text == 'add musics':
            await message.reply("qaysi qo'shiqchini qo'shmoqchisiz: ", reply_markup=add_musics)
        elif message.text == 'add videos':
            await message.reply(text="video nomini kiritng(film, serial, short video): ")
        elif message.text == 'change admins':
            await message.reply(text="qo'shiladigan admin chat_idsini kiriting:")
        elif message.text == 'back':
            await message.reply(text='➡️➡️➡️', reply_markup=menu_keyword)
    else:
        await message.reply('siz adminlik huquqiga ega emassiz')


@dp.callback_query_handler(lambda c: c.data == 'back')
async def back_callback(callback_query: types.CallbackQuery):
    await callback_query.answer()
    await bot.delete_message(chat_id=callback_query.from_user.id, message_id=callback_query.message.message_id)

"""@dp.message_handler(lambda message: message.text in ["Jaloliddin Axmadaliyev", "Yulduz Usmonova", "Baxrom Nazarov"])
async def add_musics(message: types.Message):
    data_1 = [message.text]
    data2 = message.reply(text='url linkni kiriting: ')
    data_1.append(data2)
    query = f"INSERT INTO musics(author_name, url_link) VALUES('{data_1[0]}', '{data_1[1]}');"
    db_i = Database.connect(query, 'insert')
    if db_i == "inserted successful":
        await message.reply('inserted successful')"""

"""async def add_musics(message: types.Message):
    data = []
    await message.answer(text="qo'shiq muallifini ism sharfini kiriting: ")
    data.append(message.text)
    if len(data) > 0:
        await message.reply(text="Url linkni kiriting: ")
        data.append(message.text)
    if len(data) > 1:
        query = f"INSERT INTO musics(author_name, url_link) VALUES('{data[0]}', '{data[1]}');"
        Database.connect(query, 'insert')
        await message.reply('inserted successful')
"""


@dp.message_handler(lambda message: message.text == 'Menu')
async def show_menu(message: types.Message):
    await message.answer("Menulardan birini tanlang:", reply_markup=keyboard)


@dp.callback_query_handler(lambda c: c.data in ['musics', 'videos'])
async def menu_ins(callback_query: types.CallbackQuery):
    await callback_query.answer()
    if callback_query.data == "musics":
        await bot.send_message(callback_query.from_user.id, 'choose musics', reply_markup=musics)
    else:
        await bot.send_message(callback_query.from_user.id, 'choose video', reply_markup=videos)


@dp.message_handler(lambda message: message.text == 'Category')
async def show_category(message: types.Message):
    await message.answer("Categoriyalardan birini tanlang:", reply_markup=category)


@dp.callback_query_handler(lambda c: c.data in ['music category', 'video category'])
async def category_m(callback_query: types.CallbackQuery):
    await callback_query.answer()
    if callback_query.data == "music category":
        await bot.send_message(callback_query.from_user.id, 'choose music category', reply_markup=musics_category)
    else:
        await bot.send_message(callback_query.from_user.id, 'choose video', reply_markup=videos_category)


@dp.message_handler(lambda message: message.text == 'back')
async def back_x(message: types.Message):
    await message.answer("Menulardan birini tanlang:", reply_markup=menu_keyword)


@dp.message_handler(lambda message: message.text)
async def invalid_message(message: types.Message):
    query_1 = """SELECT * FROM menu"""
    query_2 = """SELECT * FROM category"""
    query_3 = """SELECT * FROM videos"""
    query_4 = """SELECT * FROM musics"""
    data1 = Database.connect(query_1, 'select')
    data2 = Database.connect(query_2, 'select')
    data3 = Database.connect(query_3, 'select')
    data4 = Database.connect(query_4, 'select')
    if message.text not in data1[0]:
        await message.answer('invalid')
    elif message.text not in data2[0]:
        await message.answer('invalid')
    elif message.text not in data3[1]:
        await message.answer('invalid')
    elif message.text not in data4[1]:
        await message.answer('invalid')


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)



