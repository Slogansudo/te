from database_bot import Database
import telebot
import os
from dotenv import load_dotenv
data = load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")

bot = telebot.TeleBot(BOT_TOKEN)


@bot.message_handler(commands=['start', 'hello'])
def send_welcome(massage):
    first_name = massage.from_user.first_name
    last_name = massage.from_user.last_name
    username = massage.from_user.username
    bio = massage.from_user.bio
    chat_id = str(massage.chat.id)
    check_q = f"""SELECT*FROM users_data WHERE chat_id = '{chat_id}';"""
    if len(Database.connect(check_q, 'select')) >= 1:
        bot.reply_to(massage, f"Hello {massage.from_user.first_name} welcome to")
        bot.send_message(massage.from_user.id, f"my name is {bot.get_me().first_name} bot")
        bot.send_message(massage.from_user.id, f"send /data to me and I will send your data to you ")
    else:
        print(f"{first_name} start bot")
        query =f"""INSERT INTO users_data(first_name, last_name, username, chat_id, bio) VALUES (
            '{first_name}', '{last_name}', '{username}', '{chat_id}', '{bio}');"""
        print(f"{username} insert the {Database.connect(query, 'insert')} database")
        bot.reply_to(massage, f"Hello {massage.from_user.first_name} welcome to")
        bot.send_message(massage.from_user.id, f"my name is {bot.get_me().first_name} bot")
        bot.send_message(massage.from_user.id, f"send /data to me and I will send your data to you ")


@bot.message_handler(func=lambda msg: True)
def echo_all(massage):
    if massage.text == "/data":
        chat_id = massage.chat.id
        query_s = f"""SELECT * FROM users_data WHERE chat_id = '{chat_id}';"""
        data_x = Database.connect(query_s, 'select')
        bot.reply_to(massage, f"""
                Hi @{data_x[0][3]}
            first_name: {data_x[0][1]}
            last_name: {data_x[0][2]}
            bio: {data_x[0][4]}
            chat_id: {data_x[0][3]}
            
            I know this information for now """)


"""if __name__ == '__main__':
    bot.infinity_polling()
"""