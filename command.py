import sqlite3
import telebot

from telebot import types
from telebot.types import InlineKeyboardButton, InlineKeyboardMarkup

bot = telebot.TeleBot("1757847078:AAF9MlsiRs3Z1ChLzLJfrxnaA4sIPjAOIk4")
newUser = True


def start(message):
    conn = sqlite3.connect('DUral.db')
    cur = conn.cursor()

    global newUser

    setUserID = str(message.from_user.id)
    setUserName = str(message.from_user.username)

    searchID = "SELECT COUNT(DISTINCT id_user) FROM users WHERE id_user = '" + setUserID + "'; "

    cur.execute(searchID)
    results = cur.fetchone()
    # print(results)

    for i in results:
        if i == 0:
            setUserData = "INSERT INTO users VALUES ('" + setUserID + "', '" + setUserName + "', NULL, NULL, NULL, " \
                                                                                             "NULL); "
            cur.execute(setUserData)
            conn.commit()
        else:
            newUser = False

    """bot.send_message(message.chat.id, "Привет, я ... и я помогу тебе разобраться в Урале\n"
                                      "спроси меня где находиться Чердынь\n"
                                      "или где купить футболку как у Васи\n"
                                      "и постораюсь тебе помочь"
                     )"""

    send_mess = ("Привет, я ... и я помогу тебе разобраться в Урале\n"
                 "проси меня где находиться Чердынь\n"
                 "или расскажи про каменный город\n"
                 "и постораюсь тебе помочь")

    user_markup = telebot.types.ReplyKeyboardMarkup(True, False)
    user_markup.row('Где находится Хохловка')
    user_markup.row('Расскажи про Каменный город')
    bot.send_message(message.from_user.id, send_mess, reply_markup=user_markup)
