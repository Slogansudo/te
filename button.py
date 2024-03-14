from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


menu_keyword = ReplyKeyboardMarkup([
    [KeyboardButton('Menu'), KeyboardButton("Category")],
    [KeyboardButton("Types")]], resize_keyboard=True)


menu_inside = ReplyKeyboardMarkup([
    [KeyboardButton('musics'), KeyboardButton("videos")],
    [KeyboardButton('contacts')],
    [KeyboardButton('back')]], resize_keyboard=True)

musics = ReplyKeyboardMarkup([
    [KeyboardButton('Yulduz Usmonova'), KeyboardButton('Jahongir Otajonov')],
    [KeyboardButton('Baxrom Nazarov')],
    [KeyboardButton('back')]], resize_keyboard=True)

videos = ReplyKeyboardMarkup([
    [KeyboardButton('serials'), KeyboardButton('Ujas')],
    [KeyboardButton('Detective'), KeyboardButton('historical')],
    [KeyboardButton('back')]
])

category_menu = ReplyKeyboardMarkup([
    [KeyboardButton("music category"), KeyboardButton("video category")],
    [KeyboardButton("back")]], resize_keyboard=True)

musics_category = ReplyKeyboardMarkup([
    [KeyboardButton('happy'), KeyboardButton('sad')],
    [KeyboardButton('back')]], resize_keyboard=True)

videos_category = ReplyKeyboardMarkup([
    [KeyboardButton('detective'), KeyboardButton('national')],
    [KeyboardButton('world films')],
    [KeyboardButton('back')]], resize_keyboard=True)


types_menu = ReplyKeyboardMarkup([
    [KeyboardButton("interesting"), KeyboardButton("funny")],
    [KeyboardButton("back")]], resize_keyboard=True)


inter_menu = ReplyKeyboardMarkup([
    [KeyboardButton("video"), KeyboardButton("musics")],
    [KeyboardButton("back")]], resize_keyboard=True)

fun_menu = ReplyKeyboardMarkup([
    [KeyboardButton("musics"), KeyboardButton("videos")],
    [KeyboardButton("back")]], resize_keyboard=True)

romantic_menu = ReplyKeyboardMarkup([
    [KeyboardButton("videos"), KeyboardButton("musics")],
    [KeyboardButton("back")]], resize_keyboard=True)
