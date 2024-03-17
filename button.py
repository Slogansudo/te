from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from database_bot import Database

menu_keyword = ReplyKeyboardMarkup([
    [KeyboardButton('Menu'), KeyboardButton("Category")],
    ], resize_keyboard=True)


services = ReplyKeyboardMarkup([[KeyboardButton('add musics'), KeyboardButton("add videos")],
        [KeyboardButton('change admins')], [KeyboardButton('back')]], resize_keyboard=True)


"""query = f
dat = []
add_musics = ReplyKeyboardMarkup(resize_keyboard=True)
for i in Database.connect(query, 'select'):
    add_musics.add(KeyboardButton(str(i[1])))
"""
add_musics = ReplyKeyboardMarkup([[KeyboardButton('Jaloliddin Axmadaliyev'), KeyboardButton('Yulduz Usmonova')],
                                  ["Baxrom Nazarov"]], resize_keyboard=True)
