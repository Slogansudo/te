from aiogram import types

keyboard = types.InlineKeyboardMarkup(row_width=2)
button2 = types.InlineKeyboardButton(text="musics", callback_data="musics")
button1 = types.InlineKeyboardButton(text="videos", callback_data="videos")
button3 = types.InlineKeyboardButton(text="back", callback_data="back")
keyboard.add(button1, button2, button3)


m_button = types.InlineKeyboardButton(text="Yulduz Usmonova", callback_data="Yulduz Usmonova")
m_button2 = types.InlineKeyboardButton(text="Jaloliddin Axmadaliyev", callback_data="Jaloliddin Axmadaliyev")
m_button3 = types.InlineKeyboardButton(text="Baxrom Nazarov", callback_data="Baxrom Nazarov")
m_button4 = types.InlineKeyboardButton(text="back", callback_data="back")

# music
musics = types.InlineKeyboardMarkup(row_width=3)
musics.add(m_button, m_button2, m_button3, m_button4)


v_button = types.InlineKeyboardButton(text='serial', callback_data='serial')
v_button2 = types.InlineKeyboardButton(text='film', callback_data='film')
v_button3 = types.InlineKeyboardButton(text='short video', callback_data='short data')
v_button4 = types.InlineKeyboardButton(text='back', callback_data="back")

# video
videos = types.InlineKeyboardMarkup(row_width=3)
videos.add(v_button, v_button2, v_button3, v_button4)


c_button1 = types.InlineKeyboardButton(text='music category', callback_data='music category')
c_button2 = types.InlineKeyboardButton(text='video category', callback_data='video category')
c_button3 = types.InlineKeyboardButton(text='back', callback_data="back")

# category
category = types.InlineKeyboardMarkup(row_width=2)
category.add(c_button1, c_button2, c_button3)


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



