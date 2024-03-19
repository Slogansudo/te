from aiogram import types

keyboard = types.InlineKeyboardMarkup(row_width=2)
menu1 = types.InlineKeyboardButton(text="musics", callback_data="musics")
menu2 = types.InlineKeyboardButton(text="videos", callback_data="videos")
menu3 = types.InlineKeyboardButton(text="back", callback_data="back")
keyboard.add(menu1, menu2, menu3)


music_menu = types.InlineKeyboardButton(text="Yulduz Usmonova", callback_data="Yulduz Usmonova")
music_menu2 = types.InlineKeyboardButton(text="Jaloliddin Axmadaliyev", callback_data="Jaloliddin Axmadaliyev")
music_menu3 = types.InlineKeyboardButton(text="Baxrom Nazarov", callback_data="Baxrom Nazarov")
music_menu4 = types.InlineKeyboardButton(text="back", callback_data="back")

# music
musics = types.InlineKeyboardMarkup(row_width=3)
musics.add(music_menu, music_menu2, music_menu3, music_menu4)


video_menu = types.InlineKeyboardButton(text='serial', callback_data='serial')
video_menu2 = types.InlineKeyboardButton(text='film', callback_data='film')
video_menu3 = types.InlineKeyboardButton(text='short video', callback_data='short data')
video_menu4 = types.InlineKeyboardButton(text='back', callback_data="back")

# video
videos = types.InlineKeyboardMarkup(row_width=3)
videos.add(video_menu, video_menu2, video_menu3, video_menu4)


category1 = types.InlineKeyboardButton(text='music category', callback_data='music category')
category2 = types.InlineKeyboardButton(text='video category', callback_data='video category')
category3 = types.InlineKeyboardButton(text='back', callback_data="back")

# category
category = types.InlineKeyboardMarkup(row_width=2)
category.add(category1, category2, category3)


videos_category = types.InlineKeyboardMarkup(row_width=2)
video_b1 = types.InlineKeyboardButton(text='detective', callback_data='detective')
video_b2 = types.InlineKeyboardButton(text='national', callback_data='national')
video_b3 = types.InlineKeyboardButton(text='back', callback_data="back")

# c=video category
videos_category.add(video_b1, video_b2, video_b3)

musics_category = types.InlineKeyboardMarkup(row_width=2)
music_b1 = types.InlineKeyboardButton(text='happy', callback_data='happy')
music_b2 = types.InlineKeyboardButton(text='sad', callback_data="sad")
music_b3 = types.InlineKeyboardButton(text='back', callback_data="back")

musics_category.add(music_b1, music_b2, music_b3)



